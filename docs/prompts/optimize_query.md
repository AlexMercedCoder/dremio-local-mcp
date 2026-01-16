# Prompt: Optimize Query

**Name**: `optimize_query`

## Description
This prompt reviews a SQL query *before* or *after* you run it to suggest performance improvements and anti-pattern removals.

It automatically:
1.  Scans for **Anti-Patterns** (e.g. `SELECT *` on massive tables, calculated join keys).
2.  Recommends **Reflections** that would accelerate the query.
3.  Rewrites the query for **Efficiency**.

## Arguments
- `sql_query` (string): The SQL text to analyze.

## Usage Example

**User:**
> "Optimize this query: SELECT * FROM Taxi_Trips WHERE year(pickup) = 2023"

**Assistant Action:**
Returns advice:

```markdown
# Query Optimization

## Anti-Patterns Detected
- `SELECT *`: Returns unnecessary columns. Select only what you need.
- `WHERE year(pickup)`: Function on a column prevents partition pruning.

## Recommended Rewrite
```sql
SELECT passenger_count, amount 
FROM Taxi_Trips 
WHERE pickup >= '2023-01-01' AND pickup < '2024-01-01'
```
*This rewrite allows Dremio to skip reading files from other years.*
```
