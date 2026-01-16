# Semantic Tools

Tools for managing the semantic layer: creating views, documenting data, and organizing spaces.

## Tools

### `create_view(sql: str, path: str)`
Creates a virtual dataset (view) defined by a SQL query.
- **path**: Dot-delimited path (e.g., `Marketing.Campaigns.Q1_Results`).

**Prompt Examples:**
> "Create a view called 'Sales.RecentOrders' that selects all orders from last month."

### `update_wiki(entity_id: str, content: str)`
Updates the wiki markdown documentation for a dataset.
- **entity_id**: The UUID of the dataset (use `get_semantic_context` or `list_datasets` to find it).

**Prompt Examples:**
> "Update the wiki for the customers view to explain that the 'status' column is deprecated."

### `add_tags(entity_id: str, tags: list[str])`
Adds tags to a dataset to improve discoverability.
- **tags**: A list of tag strings (e.g., `["verified", "production"]`).

**Prompt Examples:**
> "Tag the sales table as 'PII' and 'Confidential'."

### `get_semantic_context(path: str)`
Resolves a path to its ID and Metadata. Useful for getting the `entity_id` needed for wiki/tag operations.

**Prompt Examples:**
> "Get the ID for 'Sales.RecentOrders' so I can update its wiki."

### `plan_semantic_layer(goal: str)`
Generates a structural proposal (ASCII tree) for a semantic layer implementation based on a goal.

**Note**: This tool automatically scans your local `~/dremiodocs` folder for relevant best practices and includes them in the generated plan.

**Sample Prompt:**
"Plan a semantic layer for our new Q4 Sales Dashboard."

**Prompt Examples:**
> "Plan a semantic layer for a retail analytics dashboard."
