# Prompt: Draft Wiki

**Name**: `draft_wiki`

## Description
This prompt automates the creation of documentation. It analyzes the technical metadata of a dataset to generate a business-friendly Wiki entry in Markdown format.

It automatically:
1.  Inspects the **Schema** to understand the data's shape.
2.  Infers the **Business Purpose** based on table and column names.
3.  Drafts a complete **Wiki** entry with Description, Column Dictionary, and Usage examples.

## Arguments
- `path` (string): The full path to the dataset.

## Usage Example

**User:**
> "Draft a wiki for the reflection_candidates table"

**Assistant Action:**
Returns a draft you can immediately approve:

```markdown
# Draft Wiki for: reflection_candidates

## Description
This dataset appears to track candidates for acceleration reflections...

## Column Dictionary
| Column | Type | Description |
|--------|------|-------------|
| dataset_id | VARCHAR | Unique identifier for the source |
| ...

*Would you like me to save this wiki now?*
```
