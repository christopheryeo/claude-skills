# Output Format

Read this reference before rendering Drive results or normalizing Drive metadata.

## File Type Labels

Convert raw MIME types into friendly labels for display:

| MIME type | Label |
|---|---|
| `application/vnd.google-apps.document` | Doc |
| `application/vnd.google-apps.spreadsheet` | Sheet |
| `application/vnd.google-apps.presentation` | Slides |
| `application/vnd.google-apps.folder` | Folder |
| `application/vnd.google-apps.form` | Form |
| `application/pdf` | PDF |
| `audio/mpeg`, `audio/*` | Audio |
| `video/mp4`, `video/*` | Video |
| `image/png`, `image/jpeg`, `image/*` | Image |
| `text/plain`, `text/csv` | Text |
| `application/zip`, `application/x-zip*` | Archive |
| All others | File |

## Timestamp Formatting

- Default timezone: Singapore / `Asia/Singapore`.
- Format full timestamps as `DD MMM YYYY, HH:MM SGT`, for example `12 Mar 2026, 08:44 SGT`.
- For compact tables, `DD MMM, HH:MM SGT` is acceptable when the surrounding header states the year.
- User timezone preferences override the default; label the chosen timezone explicitly.

## Links and Metadata

- Always embed the Drive link in the filename: `[Filename](web_view_link)`.
- If a connector returns no link but returns an ID, use the canonical link format only when the host's connector documentation supports it. Otherwise say the link was unavailable.
- Show owner only when returned by Drive metadata. Do not infer ownership from folder names or prior context.
- Keep summaries neutral and derived from file name, type, metadata, and fetched content when explicitly retrieved.

## Folder Contents Template

```markdown
# FOLDER CONTENTS
**Folder:** {folder name} | **Files:** {count} | **Retrieved:** {current date, SGT}

| # | File | Type | Last Modified | Summary |
|---|------|------|---------------|---------|
| 1 | [Filename](web_view_link) | Doc | 12 Mar 2026, 08:44 SGT | <=25-word description. |
```

If the folder is empty:

```markdown
# FOLDER CONTENTS
**Folder:** {folder name} | **Files:** 0

No files found in this folder.
```

## Recent Files Template

```markdown
# DRIVE RECENT FILES
**{Current date, SGT} | Last {X} Hours/Days**

## Summary
- **Total files found:** {count}
- **Timeframe:** Last {X} hours/days/weeks
- **Most recent:** {filename} ({time ago})
- **Oldest in list:** {filename} ({time ago})

| # | File | Type | Last Modified | Summary | Owner |
|---|------|------|---------------|---------|-------|
| 1 | [Filename](link) | Doc | 12 Mar, 08:44 SGT | <=30-word summary. | Owner Name |
```

## Topic Files Template

```markdown
# TOPIC FILES - {Topic}
**Query:** `{primary query}` | **Files found:** {count} | **Timeframe:** {range or "All available"}

## Overview
- **Scope:** {topic and filters}
- **Coverage:** {oldest} -> {newest}

## File Highlights
1. **{File Title}** - {Type} - {Owner} - {Modified Date SGT}
   - {<=40-word insight}
   - [Open in Drive]({link})

| # | File | Type | Last Modified | Summary |
|---|------|------|---------------|---------|
| 1 | [Filename](link) | Doc | 12 Mar, 08:44 SGT | <=60-word summary. |

## Next Steps
- {Actionable follow-up based on findings}
```

## Work-Day Template

```markdown
# WORK DAY - {DD Month YYYY}

| Folder | Status | Link |
|--------|--------|------|
| SNMG00 Management | Exists | [Open]({link}) |
| SNMG18 Working Docs | Exists | [Open]({link}) |
| {YYYY-MM Work} | Exists / Created | [Open]({link}) |
| {YYYY-MM-DD} | Exists / Created | [Open]({link}) |

**Structure ready.** Your work day folder is prepared.
```

## Quality Checklist

Before finalizing: sequential numbering, friendly type labels, working Drive links from API data, timezone stated, summaries within word limits, sorted appropriately, no fabricated metadata.
