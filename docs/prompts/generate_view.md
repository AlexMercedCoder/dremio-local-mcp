# Prompt: Generate View

**Name**: `generate_view`

## Description
This prompt acts as a "Semantic Layer Architect". It helps you create curated, business-ready views from raw data, following best practices (Medallion Architecture).

It automatically:
1.  Analyzes the **Source Schema**.
2.  Proposes a **SQL Definition** that:
    - Renames technical columns to business terms.
    - Casts data types.
    - Applies necessary logic for the stated goal.
3.  Suggests a logical **Path** for the new view.

## Arguments
- `goal` (string): What you want this view to achieve (e.g. "Clean up customer names and standardise dates").
- `source_path` (string): The raw table to start from.

## Usage Example

**User:**
> "Generate a view for 'Certified Customer List' from 'Raw.Extracts.Cust_Dump_v1'"

**Assistant Action:**
Returns a SQL definition for review:

```sql
-- Proposed View: Business.Customer.Certified_List
CREATE VIEW "Business"."Customer"."Certified_List" AS
SELECT
    customer_id AS Customer_ID,
    UPPER(last_name) AS Surname,
    CAST(signup_date AS DATE) AS Join_Date
FROM "Raw"."Extracts"."Cust_Dump_v1"
```
