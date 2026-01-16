# Product Requirements Document: Dremio MCP Server

## 1. Overview
The goal is to create an easy-to-use Model Context Protocol (MCP) server for Dremio. This server will enable AI agents to interact with a Dremio instance to perform semantic modeling, execute queries, analyze jobs, and manage datasets. It will verify actions against local `dremiodocs`. The server will be published to PyPI and include a CLI for configuration.

## 2. Core Features

### 2.1. Semantic Layer Management
**Goal**: Help users design and manage their semantic layer (Views, Tags, Wikis).
**Tools**:
- `create_view(sql, name, space)`: Create virtual datasets.
- `update_wiki(entity_id, content)`: Update the wiki for a dataset/source.
- `add_tags(entity_id, tags)`: Tag datasets.
- `get_semantic_context(entity_id)`: Retrieve wiki, tags, schema.
- `plan_semantic_layer(goal)`: Propose a semantic layer structure (views, spaces) based on a natural language goal. Returns an ASCII chart and definition plan.

### 2.2. Query Execution & Safety
**Goal**: Execute SQL queries safely.
**Tools**:
- `execute_query(sql, context)`: Run a SQL query.
  - **Validation**: Validate SQL syntax against `dremiodocs`.
  - **Safety check**: Destructive queries (DROP, DELETE, TRUNCATE) require user confirmation.

### 2.3. Job Analysis & Performance
**Goal**: Monitor jobs and suggest improvements.
**Tools**:
- `list_jobs(filter)`: Get recent job history.
- `analyze_job(job_id)`: Retrieve job profile.
- `recommend_performance_improvements(job_id)`: Analyze execution plan.

### 2.4. Dataset Discovery
**Goal**: Explore available data.
**Tools**:
- `list_datasets(path)`: List tables/views.
- `get_dataset_schema(path/id)`: Get columns and types.

### 2.5. Context Packaging
**Goal**: Provide rich context to the LLM.
**Tools**:
- `package_dataset_context(path/id)`: Bundle Schema, Wiki, Tags, Lineage.

### 2.6. Reflection Recommendations
**Goal**: Optimize acceleration.
**Tools**:
- `scan_reflection_opportunities()`: Scan for reflection candidates.

### 2.7. Documentation Integration
**Goal**: Use `dremiodocs` for context.
- **Search**: Index and search local `dremiodocs` folder.

## 3. Technical Requirements
- **Language**: Python (FastMCP).
- **Distribution**: PyPI package (`dremio-local-mcp`).
- **Configuration**:
    - Leverages existing `dremio-cli` profiles.
    - Reads `~/.dremio/profiles.yaml` (or `.env` as fallback).
    - **Dependency**: usage of `dremio-python-cli` logic where possible/appropriate.

## 4. User Interaction Flow
1.  **User installs**: `pip install dremio-local-mcp` (installs `dremio-python-cli` as dependency).
2.  **User configures**: Runs standard `dremio` CLI commands to create a profile (or edits `~/.dremio/profiles.yaml`).
3.  **User verifies**: `dremio-local-mcp test --profile <name>` runs a connectivity check (`SELECT 1`).
4.  **User sets up Client**: `dremio-local-mcp config` prints the JSON configuration for Claude Desktop or VS Code (Code).
5.  **User runs**: `dremio-local-mcp start --profile <name>` to launch the MCP server.

## 5. Next Steps
1.  Setup Python project.
2.  Implement `dremio_client.py` using `config.yaml`.
3.  Implement tools using FastMCP.
