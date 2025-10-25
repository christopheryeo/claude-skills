---
name: work-day-files
description: Lists files contained in a work-day folder with 40-word summaries. Uses the work-day skill to locate the appropriate folder structure (YYYY-MM Work/YYYY-MM-DD) in Google Drive, then retrieves and summarizes all files within that day folder. Accepts dates in various formats and automatically detects the correct folder level.
---

# Work Day Files

## Overview

Retrieve and summarize all files stored in a specific work-day folder within the SNMG18 Working Docs directory structure. This skill leverages the work-day skill to navigate the proper folder hierarchy and provides a formatted list of all files with 40-word summaries of their content.

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

Use **Claude's Google Drive search** (`google_drive_search`) to list all files (excluding folders) within the target day folder:
- Query: Search for all items in the day folder
- Return all file types: documents, sheets, PDFs, images, etc.
- If no files found, report "No files found in this work-day folder"

### Step 5: Analyze and Summarize Files

For each file found:

**Fetch file content**:
- For Google Docs: Use `google_drive_fetch` to retrieve document content
- For Google Sheets: Use `google_drive_search` and Google Drive API to extract content
- For PDFs and other types: Use `web_fetch` with the Google Drive share link if possible
- For images: Note filename and basic metadata, provide descriptive summary based on type

**Generate 40-word summary**:
- Analyze the actual content of each file
- Create a concise, informative summary of approximately 40 words
- Focus on key content, purpose, and main findings
- Be specific and avoid generic descriptions

### Step 6: Format and Present Results

Provide output in this format:

```
Work Day Files for [YYYY-MM-DD]

📁 Files in [YYYY-MM-DD] folder:

[File Name 1]
Summary: [40-word summary of file 1 content]

[File Name 2]
Summary: [40-word summary of file 2 content]

[File Name 3]
Summary: [40-word summary of file 3 content]

Total files: [count]
```

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
→ Lists all files with 40-word summaries

**User request**: "Show me files from October 30"
→ Uses October 30, 2025
→ Navigates to SNMG18 Working Docs/2025-10 Work/2025-10-30/
→ Lists all files with 40-word summaries

**User request**: "What files are in tomorrow's folder?"
→ Uses tomorrow's date
→ Navigates to appropriate month and day folder
→ Lists all files with 40-word summaries

**User request**: "Get files for 2025-11-15"
→ Uses November 15, 2025
→ Navigates to SNMG18 Working Docs/2025-11 Work/2025-11-15/
→ Lists all files with 40-word summaries

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

## Summary Generation Guidelines

When creating 40-word summaries:

1. **Be accurate**: Reflect the actual content, not assumptions
2. **Be concise**: Use approximately 40 words (±5 words acceptable)
3. **Be informative**: Include key points, decisions, findings, or purposes
4. **Be specific**: Avoid generic statements; reference actual content
5. **Include context**: For meeting notes, mention participants or topics; for reports, mention key metrics or conclusions
6. **For different file types**:
   - Documents: Summarize main topics and conclusions
   - Sheets: Highlight data categories, key metrics, or findings
   - Meeting notes: Note attendees, topics discussed, decisions made
   - PDFs: Summarize main content and purpose
   - Images: Describe content relevance to work context

## Dependencies

This skill depends on:
- **work-day skill**: For understanding folder structure (reference only, not called directly)
- **Google Drive integration**: For searching and accessing files
- **Date parsing**: For converting user input to ISO format
```