# Query Tools

Tools for executing SQL queries against Dremio.

## Tools

### `execute_query(sql: str, context: list[str] = None)`
Executes a SQL statement.

**Safety Mechanism**:
If the query contains destructive keywords (`DROP`, `DELETE`, `TRUNCATE`, `ALTER`), the tool will block execution. To bypass this, you must include `/* --CONFIRM-DESTRUCTION-- */` in your SQL.

**Parameters**:
- **sql**: The SQL query string.
- **context**: (Optional) List of context path elements (e.g., `["SpaceName", "Folder"]`) to set the current schema.

**Prompt Examples:**
> "Run `SELECT * FROM sys.version`"
> "Execute this query using 'Marketing' context: `SELECT count(*) FROM leads`"
> "Delete the table 'Scratch.old_data'." (Will trigger safety block)
> "/* --CONFIRM-DESTRUCTION-- */ DROP TABLE Scratch.old_data" (Will proceed)
