# Job & Reflection Tools

Tools for monitoring job execution and optimizing performance.

## Job Tools

### `list_jobs(filter_str: str = "")`
Lists the 10 most recent jobs.
- **filter_str**: (Optional) Filter criteria (currently unused, lists recent).

### `analyze_job(job_id: str)`
Retrieves detailed statistics for a specific job (Rows scanned, Duration, Query Text).

### `recommend_performance_improvements(job_id: str)`
Analyzes a job's profile and suggests optimizations (e.g., adding reflections, checking for spills).

## Reflection Tools

### `scan_reflection_opportunities()`
Analyzes usage patterns to suggest datasets that would benefit from hardware acceleration (Reflections).
