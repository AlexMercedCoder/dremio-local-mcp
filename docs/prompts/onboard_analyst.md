# Prompt: Onboard Analyst

**Name**: `onboard_analyst`

## Description
This prompt is designed to help new users orient themselves within a specific Space (folder/project). It provides a guided tour of the most important assets.

It automatically:
1.  **Lists** contents of the space.
2.  **Samples** context from top datasets to identify "Gold" (high-value) vs "Bronze" (raw) data.
3.  Produces a **Getting Started Guide** for that space.

## Arguments
- `space_path` (string): The path to the Space or Folder to explore.

## Usage Example

**User:**
> "Onboard me to the Marketing space"

**Assistant Action:**
Returns a guide:

```markdown
# Onboarding Guide: Marketing Space

## Key Datasets
- 🌟 **Marketing.Campaigns.ROI_Summary**: High-value aggregated view. Start here.
- 📂 **Marketing.Raw.Clicks**: Raw clickstream logs. Use for deep dives only.

## Getting Started
To calculate last month's ROI, query `ROI_Summary` filtering by `Month_Year`.
```
