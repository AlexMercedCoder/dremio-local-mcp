# Prompt: Audit Users

**Name**: `audit_users`

## Description
This prompt answers the "Who uses this?" question. It scans job history to identify the users engaging with a specific dataset.

It automatically:
1.  Check **Job History** for the dataset.
2.  Extracts and aggregates **User** identities.
3.  Summarizes recent activity levels.

## Arguments
- `dataset_path` (string): The dataset to audit.

## Usage Example

**User:**
> "Audit users for HR.Employees"

**Assistant Action:**
Returns an access report:

```markdown
# User Audit: HR.Employees (Last 30 Days)

- **alice@example.com**: 15 queries (Heavy User)
- **bob@example.com**: 2 queries (Ad-hoc)
- **service_account_tableau**: 150 queries (Automated)

*Note: Verify if Bob should have access to this sensitive data.*
```
