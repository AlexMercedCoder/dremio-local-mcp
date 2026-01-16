# MCP Client Configuration

This guide covers how to configure common MCP clients to use the `dremio-local-mcp` server.

## Standard IO (Stdio) Transport

`dremio-local-mcp` uses standard input/output (Stdio) to communicate. This is the most common method for local MCP servers.

### General Configuration

Most clients require a JSON configuration defining the command to start the server.

**Command:** `dremio-local-mcp`
**Arguments:** `start` (or `start --profile software`)
**Env Vars:** (Optional, if profile not set in args) `DREMIO_PROFILE=cloud`

---

## Claude Desktop App

To use Dremio with Claude on your desktop:

1.  Open your Claude Desktop config file:
    - **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
    - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

2.  Add the `dremio` server entry.

### Option A: Using `uvx` (Recommended for Zero-Install)
If you have `uv` installed, this ensures you always use the latest version.

```json
{
  "mcpServers": {
    "dremio": {
      "command": "uvx",
      "args": [
        "dremio-local-mcp",
        "start"
      ],
      "env": {
        "DREMIO_PROFILE": "cloud"
      }
    }
  }
}
```

### Option B: Using `pip` / System Install
If you installed via `pip install dremio-local-mcp`:

```json
{
  "mcpServers": {
    "dremio": {
      "command": "dremio-local-mcp",
      "args": ["start"],
      "env": {
        "DREMIO_PROFILE": "software"
      }
    }
  }
}
```

### Option C: Development Mode (Running from Source)
If you are developing the server locally:

```json
{
  "mcpServers": {
    "dremio-dev": {
      "command": "uv",
      "args": [
        "run",
        "dremio-local-mcp",
        "start"
      ],
      "cwd": "/absolute/path/to/dremio-local-mcp",
      "env": {
        "DREMIO_PROFILE": "cloud"
      }
    }
  }
}
```

---

## Cursor (Experimental)

As of early 2026, Cursor and other editors are adding MCP support. Look for strict "Stdio" configuration options.

If configuring a generic "MCP Server" in an IDE:
- **Server Name:** `dremio-mcp`
- **Transport:** `stdio`
- **Command:** `uvx dremio-local-mcp start`

---

## Testing Connectivity

You can verify the configuration by asking the client:
> "List my Dremio datasets"

If configured correctly, the client should start the server process and call `list_datasets`.
