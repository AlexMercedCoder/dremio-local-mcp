from fastmcp import FastMCP, Context
from dremio_mcp.utils.dremio_client import DremioClient

def register(server: FastMCP, client: DremioClient):
    
    @server.tool()
    def list_datasets(path: str = None) -> str:
        """
        List datasets and folders at the specified path (or root if None).
        Path should be dot-delimited (e.g., "Space.Folder").
        """
        try:
            # If path is provided, get by path, otherwise list root (catalogs/sources/spaces)
            if path:
                # Dremio API uses path list for by-path
                path_list = path.split(".")
                data = client.get_catalog_item(path=path_list)
                
                output = [f"Contents of {path}:"]
                children = data.get("children", [])
                if not children:
                    return f"Contents of {path}:\n(Empty)"
                    
                for child in children:
                    c_type = child.get("type", "UNKNOWN")
                    # path is a list in children usually? No, it's just 'path' list
                    c_path = ".".join(child.get("path", []))
                    output.append(f"- [{c_type}] {c_path}")
                return "\n".join(output)
            
            else:
                # List root containers
                # We need a different endpoint for root, usually just getting catalog
                # But client.get_catalog_item(None) might not work as intended for root.
                # Let's check Dremio API... usually /api/v3/catalog lists root
                data = client._request("GET", "catalog")
                output = ["Root Catalog:"]
                for item in data.get("data", []):
                     c_type = item.get("type", "UNKNOWN")
                     c_path = ".".join(item.get("path", []))
                     output.append(f"- [{c_type}] {c_path}")
                return "\n".join(output)

        except Exception as e:
            return f"Error listing datasets: {e}"

    @server.tool()
    def get_dataset_schema(path: str) -> str:
        """
        Get the schema (columns and data types) for a dataset.
        Path should be dot-delimited.
        """
        try:
            path_list = path.split(".")
            data = client.get_catalog_item(path=path_list)
            
            # Check if it's a dataset
            if data.get("entityType") != "dataset":
                return f"Error: {path} is a {data.get('type')}, not a dataset."
                
            fields = data.get("fields", [])
            output = [f"Schema for {path}:"]
            for field in fields:
                name = field.get("name")
                type_info = field.get("type", {}).get("name")
                output.append(f"- {name}: {type_info}")
            
            return "\n".join(output)

        except Exception as e:
            return f"Error getting schema: {e}"

    @server.tool()

    def get_context(path: str) -> str:
        """
        Get comprehensive context for a dataset, including schema, wiki, and tags.
        Path should be dot-delimited.
        """
        try:
            path_list = path.split(".")
            data = client.get_catalog_item(path=path_list)
            
            entity_id = data.get("id")
            if not entity_id:
                return f"Error: Could not find ID for {path}"

            # 1. Schema
            schema_str = "Schema not available or not a dataset."
            if data.get("entityType") == "dataset":
                fields = data.get("fields", [])
                schema_lines = []
                for field in fields:
                    name = field.get("name")
                    type_info = field.get("type", {}).get("name")
                    schema_lines.append(f"- {name}: {type_info}")
                if schema_lines:
                    schema_str = "\n".join(schema_lines)
                else:
                    schema_str = "(No schema fields found)"

            # 2. Wiki
            wiki_content = "(No wiki text)"
            try:
                wiki = client.client.get_wiki(entity_id)
                wiki_content = wiki.get("text", "(No wiki text)")
            except:
                pass
                 
            # 4. Tags
            tags_content = "(No tags)"
            try:
                tags = client._request("GET", f"catalog/{entity_id}/collaboration/tag")
                tags_list = tags.get("tags", [])
                if tags_list:
                    tags_content = ", ".join(tags_list)
            except:
                pass

            return f"""
# Context for {path}

## Tags
{tags_content}

## Wiki
{wiki_content}

## Schema
{schema_str}
"""
        except Exception as e:
            return f"Error packaging context: {e}"

    @server.tool()
    def upload_dataset(local_path: str, dataset_name: str, file_format: str = "csv") -> str:
        """
        Upload a local file (reference it) by reading its content.
        This allows the agent to use local file content in its tasks.
        
        Args:
            local_path: Absolute path to the local file.
            dataset_name: Name to give the reference.
            file_format: 'csv', 'json', or 'parquet'.
        """
        import os
        if not os.path.exists(local_path):
            return f"Error: File not found at {local_path}"
            
        try:
            # For now, we just read the file to allow the LLM to 'see' it.
            # In a full implementation, this could use PyArrow/Flight to upload to Dremio.
            with open(local_path, "r") as f:
                content = f.read(20000) # Read up to 20k chars
                if len(content) == 20000:
                    content += "\n... (truncated)"
            return f"File Content for '{dataset_name}' ({local_path}):\n\n{content}"
        except Exception as e:
            return f"Error reading file: {e}"
