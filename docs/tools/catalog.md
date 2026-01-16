# Catalog Tools

Tools for exploring and understanding the datasets available in Dremio.

## Tools

### `list_datasets(path: str = None)`
Lists the contents of a Space, Source, or Folder. If `path` is omitted, it lists the root spaces and sources.

**Prompt Examples:**
> "Show me what datasets are in the 'Sales.Raw' folder."
> "List all available spaces."

### `get_dataset_schema(path: str)`
Retrieves the column names and data types for a specific dataset (Table or View).

**Prompt Examples:**
> "What columns are in 'Sales.daily_transactions'?"
> "Get the schema for the customers table."

### `package_dataset_context(path: str)`
Retrieves a comprehensive bundle of information for a dataset, including:
- **Schema**: Columns and types.
- **Wiki**: Documentation written by users.
- **Tags**: Metadata tags.

Use this before writing queries to understand the data's context and meaning.

**Prompt Examples:**
> "Give me the full context for 'Marketing.campaign_results' so I can write a query."
> "Package the context for the employees view."

### `upload_dataset`
Reference a local file by reading its content into the context. This essentially "uploads" the file's information to the agent's working memory.

**Args:**
- `local_path`: Absolute path to the local file.
- `dataset_name`: Name to give (for reference).
- `file_format`: 'csv', 'json', or 'parquet'.

**Sample Prompt:**
"Here is a CSV file at /tmp/data.csv. Can you upload and analyze it?"
