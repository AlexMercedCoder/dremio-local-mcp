import sys
import os
import asyncio
from fastmcp import FastMCP
from dremio_mcp.tools import catalog, semantic
from dremio_mcp.config import DremioConfig
from dremio_mcp.utils.dremio_client import DremioClient

# Mock or Real Client
class MockClient:
    def __init__(self):
        self.client = self
    def _request(self, *args, **kwargs): return {}
    def get_catalog_item(self, path): return {}

async def main():
    server = FastMCP("test")
    client = MockClient()
    catalog.register(server, client)
    semantic.register(server, client)
    
    print("Server Attributes:", dir(server))
    
    # Check if we can find the tools in the internal dict
    # Usually it's in server._tool_manager or similar
    
if __name__ == "__main__":
    asyncio.run(main())
