# CLI Reference

The `dremio-local-mcp` CLI manages the server and configuration.

## Commands

### `start`
Starts the MCP server.

```bash
dremio-local-mcp start [--profile <name>]
```
- **--profile**: (Optional) The name of the profile in `~/.dremio/profiles.yaml` to use. Defaults to `default`.

### `test`
Runs a connectivity check (`SELECT 1`).

```bash
dremio-local-mcp test [--profile <name>]
```
- **--profile**: (Optional) The profile to test.

### `config`
Generates the JSON configuration block required for `claude_desktop_config.json`.

```bash
dremio-local-mcp config [--profile <name>]
```

**Output Example:**
```json
{
  "mcpServers": {
    "dremio": {
      "command": "dremio-local-mcp",
      "args": [
        "start",
        "--profile",
        "default"
      ]
    }
  }
}
```
