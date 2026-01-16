# Prompt: Troubleshoot Job

**Name**: `troubleshoot_job`

## Description
This prompt diagnoses a specific failed or slow job. It acts as an automated "Level 1 Support" engineer.

It automatically:
1.  **Analyzes** the Job Profile to find error messages and stats.
2.  Checks for **Performance Bottlenecks** (spills, long scans).
3.  Explains the **Root Cause**.
4.  Suggests specific **Fixes** (SQL rewrite, Indexing/Reflection).

## Arguments
- `job_id` (string): The Dremio Job ID to analyze.

## Usage Example

**User:**
> "Troubleshoot job 1234-abcd-5678"

**Assistant Action:**
Returns a diagnostic:

```markdown
# Job Analysis: 1234-abcd-5678
**Status**: FAILED

## Root Cause
Available memory was insufficient for the sort operation, causing a spill that exceeded limits.

## Recommendations
1. **Reflection**: Create a Raw Reflection on `Dataset_X` sorted by `UserID`.
2. **Query**: Try reducing the columns in the `ORDER BY` clause.
```
