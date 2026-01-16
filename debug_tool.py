from fastmcp import FastMCP
import asyncio

async def main():
    server = FastMCP("test")
    
    @server.tool()
    def my_tool(x: int) -> int:
        return x * 2
        
    tool = await server.get_tool("my_tool")
    print(f"Tool Object: {tool}")
    print(f"Tool Type: {type(tool)}")
    print(f"Tool Dir: {dir(tool)}")
    
    # Try calling it
    try:
        res = await tool.run(x=21)
        print(f"Run Result: {res}")
    except Exception as e:
        print(f"Run failed: {e}")
        
    # Try calling fn directly
    try:
        res = tool.fn(x=21)
        print(f"FN Result: {res}")
    except Exception as e:
        print(f"FN failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
