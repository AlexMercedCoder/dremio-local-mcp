# Prompt: Find Unused Assets

**Name**: `find_unused_assets`

## Description
This prompt helps with housekeeping. It identifies datasets in a Space that have not been queried recently, flagging them as candidates for archival or cleanup.

It automatically:
1.  **Lists** all datasets in a location.
2.  Cross-references with **Job History**.
3.  Flags items with **Zero Activity**.

## Arguments
- `space_path` (string): The Space to clean up.

## Usage Example

**User:**
> "Find unused assets in Scratch_Space"

**Assistant Action:**
Returns a cleanup list:

```markdown
# Housekeeping Report: Scratch_Space

## 🧟 Zombie Assets (No access in 30 days)
- `Scratch_Space.tmp_join_test_23`
- `Scratch_Space.alice_test_view`

## 🟢 Active Assets
- `Scratch_Space.Daily_Load_Staging` (Accessed yesterday)
```
