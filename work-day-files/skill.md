---
name: work-day-files
description: Lists files contained in a work-day folder while delegating formatting to the list-files skill. Uses the work-day skill to locate the appropriate folder structure (YYYY-MM Work/YYYY-MM-DD) in Google Drive, then passes the target folder to list-files for table generation. Accepts dates in various formats and automatically detects the correct folder level.
---

# Work Day Files

## Overview

Retrieve and summarize all files stored in a specific work-day folder within the SNMG18 Working Docs directory structure. This skill leverages the work-day skill to navigate the proper folder hierarchy and delegates presentation entirely to the list-files skill, ensuring consistent catalog formatting.

## Target Directory Structure

```
Google Drive Root
└── SNMG00 Management/
    └── SNMG18 Working Docs/
        └── YYYY-MM Work/     (e.g., 2025-10 Work for October 2025)
            └── YYYY-MM-DD/   (e.g., 2025-10-25 for October 25, 2025)
                └── [FILES]   ← Files are listed and summarized from here
```

## Usage

When invoked, accept a date parameter:
- If user provides a date (e.g., "tomorrow", "October 30", "2025-11-15"), use that date
- If no date specified, default to today's date
- Accept dates in any format and convert to YYYY-MM-DD format internally

## Workflow

Execute these steps in order:

### Step 1: Determine Target Date

Convert the user's input (or today's date if not specified) to ISO 8601 format (YYYY-MM-DD).

For date parsing:
- Relative dates: "today", "tomorrow", "yesterday"
- Natural language: "October 30", "next Monday"
- ISO format: "2025-11-15"
- Other formats: Intelligently parse common date formats

### Step 2: Verify Parent Folders

Use **Claude's Google Drive search** (`google_drive_search`) to search for "SNMG00 Management" folder in Google Drive root:
- If not found, report error to user and stop
- If found, note the folder ID and proceed to next step

Use **Claude's Google Drive search** (`google_drive_search`) to search for "SNMG18 Working Docs" folder inside "SNMG00 Management":
- If not found, report error to user and stop
- If found, note the folder ID and proceed to next step

### Step 3: Locate Month and Day Folders

Convert target date to YYYY-MM format (e.g., 2025-10) for month folder name with " Work" suffix.

Use **Claude's Google Drive search** (`google_drive_search`) to search for the month folder (YYYY-MM Work) inside "SNMG18 Working Docs":
- If not found, report that no work folder exists for that month and stop
- If found, note the folder ID and proceed

Use **Claude's Google Drive search** (`google_drive_search`) to search for the day folder (YYYY-MM-DD) inside the month folder:
- If not found, report that no folder exists for that specific day and stop
- If found, note the folder ID and proceed to next step

### Step 4: List Files in Day Folder

Use **Claude's Google Drive search** (`google_drive_search`) to confirm the target day folder contains files (exclude folders). Capture the folder ID for the next step. If no files are present, report "No files found in this work-day folder" and stop.

### Step 5: Delegate Formatting to `list-files`

Once the day folder ID is confirmed, call the `list-files` skill to generate the final catalog:

- Pass the folder ID as the `scope` parameter (non-recursive).
- Set `limit` high enough to cover all files in the folder (e.g., 30) unless the user specifies otherwise.
- Choose `summary_length` = `detailed` so the table provides sufficient context.
- Default `sort_by` to `modifiedTime desc` unless the user requests a different ordering.
- Mention any filters (e.g., exclude folders) when invoking `list-files`.

Embed the returned Markdown table from `list-files` directly in the response without additional formatting or summaries. Do not append custom file descriptions, counts, or alternative layouts—`list-files` output should stand alone as the complete answer.

## Tool Usage Notes

**For searching folders and files**: Use Claude's native Google Drive integration
- `google_drive_search` - to find folders and list files within them
- Query format examples:
  - Find folder: `name = '2025-10 Work' and '${SNMG18_ID}' in parents`
  - List files: `'${DAY_FOLDER_ID}' in parents and mimeType != 'application/vnd.google-apps.folder'`

**For retrieving content**: Use Claude's native integrations
- `google_drive_fetch` - to retrieve full content of Google Docs
- `web_fetch` - to retrieve content from shared Google Drive links (for PDFs, etc.)

**For date conversion**: Use native date parsing or the reverse-date skill if needed

## Example Usage

**User request**: "List files for today"
→ Uses today's date (e.g., 2025-10-26)
→ Navigates to SNMG18 Working Docs/2025-10 Work/2025-10-26/
→ Returns the `list-files` Markdown table for that folder

**User request**: "Show me files from October 30"
→ Uses October 30, 2025
→ Navigates to SNMG18 Working Docs/2025-10 Work/2025-10-30/
→ Returns the `list-files` Markdown table for that folder

**User request**: "What files are in tomorrow's folder?"
→ Uses tomorrow's date
→ Navigates to appropriate month and day folder
→ Returns the `list-files` Markdown table for that folder

**User request**: "Get files for 2025-11-15"
→ Uses November 15, 2025
→ Navigates to SNMG18 Working Docs/2025-11 Work/2025-11-15/
→ Returns the `list-files` Markdown table for that folder

## Date Format Reference

Input format (user-provided) - any of these formats are accepted:
- Relative: "today", "tomorrow", "yesterday"
- Natural: "October 30", "next Monday", "last Friday"
- ISO: "2025-11-15", "2025/11/15"
- Other: "30 October 2025", "Oct 30", etc.

Internal format (used for navigation):
- **Month folder**: YYYY-MM Work (e.g., 2025-10 Work, 2025-11 Work)
- **Day folder**: YYYY-MM-DD (e.g., 2025-10-25, 2025-11-03)

## Error Handling

**Missing parent folders**: If "SNMG00 Management" or "SNMG18 Working Docs" folders don't exist, report error and stop.

**Missing work month folder**: If the YYYY-MM Work folder doesn't exist for the requested date, report that no work folders exist for that month.

**Missing work day folder**: If the YYYY-MM-DD folder doesn't exist for the requested date, report that no folder exists for that specific day.

**Empty folder**: If the day folder exists but contains no files, report that no files are present.

**File access issues**: If a file cannot be accessed or summarized, note the filename and indicate that the summary could not be generated due to access restrictions or file type limitations.

## Alignment with `list-files`

- Allow `list-files` to handle all summarization and metadata enrichment.
- Do not manually rewrite or extend the table output after `list-files` responds.
- If the caller needs adjustments (different limit, sort, or filters), reinvoke `list-files` with updated parameters instead of editing the table manually.

## Dependencies

This skill depends on:
- **work-day skill**: For understanding folder structure (reference only, not called directly)
- **Google Drive integration**: For searching and accessing files
- **Date parsing**: For converting user input to ISO format