# Prompt: Analyze Dataset

**Name**: `analyze_dataset`

## Description
This prompt generates a comprehensive status report for a given dataset. It acts as an automated "health check" or "briefing" for an analyst.

It automatically:
1.  Retrieves the **Schema** (`get_dataset_schema`) to show columns and types.
2.  Fetches existing **Context** (`get_context`) like Wiki documentation and Tags.
3.  Checks for recent **Performance** or operational issues (`list_jobs` / `recommend_performance_improvements`).

## Arguments
- `path` (string): The full path to the dataset (e.g., `Samples."samples.dremio.com"."NYC-taxi-trips"`).

## Usage Example

**User:**
> "Run the analyze dataset prompt for Samples.NYC-taxi-trips"

**Assistant Action:**
The assistant will execute the prompt logic and return a structured report:

```markdown
# Analysis Report: Samples.NYC-taxi-trips

## 1. Schema Overview
- `pickup_datetime` (TIMESTAMP)
- `passenger_count` (INTEGER)
...

## 2. Documentation Status
- **Wiki**: Found. (Preview: "Contains taxi trips from...")
- **Tags**: `transportation`, `public-data`

## 3. Operational Health
- **Recent Jobs**: 5 queries in last 24h.
- **Recommendations**: No recent failures. Consider partitioning by year.
```
