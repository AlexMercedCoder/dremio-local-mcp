from fastmcp import FastMCP
from dremio_mcp.utils.dremio_client import DremioClient
import json

def register(server: FastMCP, client: DremioClient):

    @server.tool()
    def create_view(sql: str, path: str) -> str:
        """
        Create a new virtual dataset (view) at the specified path.
        path should be dot-delimited (e.g., "Space.Folder.NewViewName").
        """
        try:
            path_list = path.split(".")
            client.create_view(sql, path_list)
            return f"Successfully created view at {path}"
        except Exception as e:
            return f"Error creating view: {e}"

    @server.tool()
    def update_wiki(entity_id: str, content: str) -> str:
        """
        Update the wiki documentation for a dataset.
        entity_id: The ID of the dataset (use get_dataset_schema or list_datasets to find ID, or just use path tools to look it up first).
        """
        try:
            # Endpoint: /api/v3/catalog/{id}/collaboration/wiki
            payload = {"text": content}
            client._request("POST", f"catalog/{entity_id}/collaboration/wiki", json=payload)
            return f"Successfully updated wiki for {entity_id}"
        except Exception as e:
            return f"Error updating wiki: {e}"

    @server.tool()
    def add_tags(entity_id: str, tags: list[str]) -> str:
        """
        Add tags to a dataset.
        tags: List of strings.
        """
        try:
            # Endpoint: /api/v3/catalog/{id}/collaboration/tag
            # Need to get existing tags first to merge? Or does POST overwrite?
            # Typically POST overwrites or merges. Dremio API behavior: POST replaces.
            # So we should get existing first.
            try:
                current = client._request("GET", f"catalog/{entity_id}/collaboration/tag")
                existing_tags = current.get("tags", [])
            except:
                existing_tags = []
            
            new_tags = list(set(existing_tags + tags))
            payload = {"tags": new_tags}
            client._request("POST", f"catalog/{entity_id}/collaboration/tag", json=payload)
            return f"Successfully updated tags. Current tags: {new_tags}"
        except Exception as e:
            return f"Error adding tags: {e}"

    @server.tool()
    def get_semantic_context(path: str) -> str:
        """
        Retrieve semantic info (ID, Path, Type) for a path to help with IDs for other tools.
        """
        try:
            path_list = path.split(".")
            data = client.get_catalog_item(path=path_list)
            return json.dumps({
                "id": data.get("id"),
                "path": data.get("path"),
                "type": data.get("type"),
                "entityType": data.get("entityType")
            }, indent=2)
        except Exception as e:
            return f"Error resolving path: {e}"


    @server.tool()
    def plan_semantic_layer(goal: str) -> str:
        """
        Propose a semantic layer structure (Spaces, Folders, Views) based on a high-level goal.
        Returns an ASCII tree and a text description of the plan.
        
        This tool automatically scans your local `~/dremiodocs` folder for relevant best practices.
        """
        try:
             # Import helper inside function to avoid circular deps if any
             from dremio_mcp.utils.docs_helper import query_docs
             docs_context = query_docs(goal) or query_docs("best practices") or ""
        except:
             docs_context = "(Docs integration unavailable)"

        prompt = f"""
# Semantic Layer Plan: {goal}

{docs_context}

## Proposed Structure (ASCII)

Raw (Bronze)
├── /raw/landing (original files)
└── /raw/staging (cleaned PDS)

Refined (Silver)
├── /business/sales_orders (Joined VDS)
└── /business/customers (Cleaned VDS)

Curated (Gold)
├── /app/dashboard_q4 (Aggregated VDS for reporting)

## Next Steps
1. Use `create_view` to build the Silver layer.
2. Verify data with `execute_query`.
3. Document with `update_wiki`.
"""
        return prompt
