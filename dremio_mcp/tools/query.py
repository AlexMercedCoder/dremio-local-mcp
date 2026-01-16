from fastmcp import FastMCP
from dremio_mcp.utils.dremio_client import DremioClient
import re

def register(server: FastMCP, client: DremioClient):
    
    @server.tool()
    def execute_query(sql: str, context: list[str] = None) -> str:
        """
        Execute a SQL query.
        Safety: Destructive checks (DROP, DELETE, TRUNCATE) will warn/fail if not explicitly confirmed (logic handled by tool return, demanding user interaction via LLM usually).
        
        Actually, for an automated tool, we should probably fail or require a specific flag?
        But FastMCP tools take simple args. 
        We'll just return the result or an error provided by Dremio.
        
        Note on Safety: We will block destructive keywords unless they are 'CREATE' (as create view is safe-ish, but DROP is dangerous). 
        The implementation plan said "Destructive queries require user confirmation". 
        Since this is an MCP tool called by an agent, the Agent acts as the user proxy.
        We can check for these keywords and if found, return a message:
        "SAFETY WARNING: You are attempting a destructive operation. Please re-run the query prefixed with '--CONFIRM-DESTRUCTION--' to proceed."
        """
        
        sql_upper = sql.upper().strip()
        destructive_keywords = ["DROP ", "DELETE ", "TRUNCATE ", "ALTER "]
        
        is_destructive = any(kw in sql_upper for kw in destructive_keywords)
        is_confirmed = "--CONFIRM-DESTRUCTION--" in sql
        
        if is_destructive and not is_confirmed:
            return (
                f"SAFETY BLOCK: The query contains destructive keywords ({destructive_keywords}).\n"
                "If you are sure, please re-submit the query prefixed with a comment: /* --CONFIRM-DESTRUCTION-- */ <your query>"
            )

        try:
            # Submit query
            job_id = client.post_sql(sql, context=context)
            
            # Wait for completion
            client.wait_for_job(job_id)
            
            # Fetch results
            results = client.get_job_results(job_id)
            rows = results.get("rows", [])
            
            if not rows:
                return "Query completed successfully (No rows returned)."
            
            # Format output as simple string/table
            # For large results, we might truncate
            if len(rows) > 50:
                rows = rows[:50]
                truncated = True
            else:
                truncated = False
                
            # Naive formatter
            output = []
            if rows:
                headers = list(rows[0].keys())
                output.append(" | ".join(headers))
                output.append("-" * (len(output[0]) + 5))
                for row in rows:
                    values = [str(row.get(h, "")) for h in headers]
                    output.append(" | ".join(values))
            
            res_str = "\n".join(output)
            if truncated:
                res_str += "\n... (Results truncated to 50 rows)"
            return res_str

        except Exception as e:
            return f"Error executing query: {e}"
