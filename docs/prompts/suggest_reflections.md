# Prompt: Suggest Reflections

**Name**: `suggest_reflections`

## Description
This prompt analyzes a dataset and suggests the optimal Reflections to create to accelerate downstream queries.

It automatically:
1.  Simulates a **Workload Analysis** (via `scan_reflection_opportunities`).
2.  Proposes **Raw Reflections** for row-level lookups.
3.  Proposes **Aggregation Reflections** for BI dashboards.
4.  Generates the **DDL** statements.

## Arguments
- `dataset_path` (string): The dataset to accelerate.

## Usage Example

**User:**
> "Suggest reflections for Sales.Transactions"

**Assistant Action:**
Returns configuration SQL:

```sql
-- Recommended Aggregation Reflection (for Dashboards)
ALTER DATASET "Sales"."Transactions" 
CREATE AGGREGATION REFLECTION "Agg_By_Region"
USING
DIMENSIONS (Region, Transaction_Date)
MEASURES (Amount);

-- Recommended Raw Reflection (for Detail Lookups)
ALTER DATASET "Sales"."Transactions"
CREATE RAW REFLECTION "Raw_Detail"
USING DISPLAY (Transaction_ID, Customer_ID, Amount)
DISTRIBUTE BY (Customer_ID);
```
