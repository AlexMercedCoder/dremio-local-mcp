# Prompt: Compare Schemas

**Name**: `compare_schemas`

## Description
This prompt performs a diff between two datasets. It is essential for verifying changes between environments (e.g., Development vs. Production) or tracking schema evolution over time.

It automatically:
1.  Fetches schemas for **Dataset A** and **Dataset B**.
2.  Identifies **Added**, **Removed**, or **Changed** columns.
3.  Outputs a comparison table.

## Arguments
- `path_a` (string): Path to the first dataset (e.g. `Dev.MyTable`).
- `path_b` (string): Path to the second dataset (e.g. `Prod.MyTable`).

## Usage Example

**User:**
> "Compare schemas for Dev.Customers and Prod.Customers"

**Assistant Action:**
Returns a diff report:

```markdown
# Schema Comparison

| Column | Dev | Prod | Status |
|--------|-----|------|--------|
| `email` | VARCHAR | VARCHAR | ✅ Match |
| `phone` | VARCHAR | - | 🆕 New in Dev |
| `age` | INTEGER | VARCHAR | ⚠️ Type Mismatch |
```
