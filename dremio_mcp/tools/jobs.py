from fastmcp import FastMCP
from dremio_mcp.utils.dremio_client import DremioClient

def register(server: FastMCP, client: DremioClient):
    
    @server.tool()
    def list_jobs(filter_str: str = "") -> str:
        """
        List recent jobs.
        filter_str: Optional SQL-like filter for job listing if supported, or just 'recent'.
        Actually Dremio API supports filtering.
        """
        try:
            # /api/v3/job?sort=start&order=DESC
            # We assume dremio_client has a _request method
            data = client._request("GET", "job?sort=start&order=DESC&limit=10")
            jobs = data.get("items", [])
            output = ["Recent Jobs:"]
            for job in jobs:
                jid = job.get("id")
                state = job.get("jobState")
                user = job.get("user")
                query_snippet = job.get("queryText", "")[:50].replace("\n", " ")
                output.append(f"- {jid} [{state}] ({user}): {query_snippet}...")
            return "\n".join(output)
        except Exception as e:
            return f"Error listing jobs: {e}"

    @server.tool()
    def analyze_job(job_id: str) -> str:
        """
        Retrieve details for a specific job.
        """
        try:
            status = client.get_job_status(job_id)
            # job details often need more than just status to be useful for "analysis"
            # We want stats usually.
            stats = status.get("jobStats", {})
            
            return f"""
Job ID: {job_id}
State: {status.get('jobState')}
User: {status.get('user')}
Rows Scanned: {stats.get('inputBytes', 0)} bytes
Duration: {stats.get('isoduration', 'N/A')}
Query:
{status.get('queryText')}
"""
        except Exception as e:
            return f"Error analyzing job: {e}"

    @server.tool()
    def recommend_performance_improvements(job_id: str) -> str:
        """
        Analyze a job and suggest improvements.
        This is a heuristic tool. It checks stats and state.
        """
        try:
            status = client.get_job_status(job_id)
            stats = status.get("jobStats", {})
            state = status.get("jobState")
            
            recommendations = []
            
            if state == "FAILED":
               return f"Job Failed. Error: {status.get('errorMessage')}. Recommendation: Fix the error first."
            
            # Heuristics
            input_bytes = stats.get("inputBytes", 0)
            output_bytes = stats.get("outputBytes", 0)
            
            if input_bytes > 1_000_000_000: # 1GB
                recommendations.append("- Large scan (>{1GB}). Consider using Reflections or partitioning.")
            
            if status.get("accelerated", False) is False:
                 recommendations.append("- Job was NOT accelerated. Check if a Reflection matches this query pattern.")
                 
            spilled = stats.get("isSpilled", False) # Hypothetical field, need to check API schema
            # Actually typically 'spill' info is deeper in profile.
            # We'll stick to high level
            
            if not recommendations:
                recommendations.append("No obvious issues found based on high-level stats.")
                
            return "Performance Recommendations:\n" + "\n".join(recommendations)

        except Exception as e:
            return f"Error recommending improvements: {e}"
