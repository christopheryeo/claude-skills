# Recent Workflow

Use this workflow to discover recently modified or created files across Google Drive.

## Defaults

- Default timeframe: last 24 hours.
- Default result cap: 20 files.
- Default sorting: most recently modified first.

## Steps

1. Determine the timeframe.
   - Use the user's explicit range when provided: "last 3 hours", "last 7 days", "since Monday", "today", and similar.
   - Otherwise use the last 24 hours.
   - Convert the start boundary to an ISO 8601 timestamp in `Asia/Singapore` unless the user requested another timezone.
2. Search Drive for recent files.
   - Use the native Drive search operation.
   - Prefer a Drive filter like `modifiedTime > '{iso_timestamp}' and trashed = false`.
   - Exclude folders unless the user asks to include folder activity.
   - Request up to 20 displayed files; if the connector reports more results, mention the result is capped.
3. Enrich results.
   - Map MIME type to a friendly type label using `output-format.md`.
   - Convert timestamps to the selected timezone.
   - Generate <=30-word summaries from filename, type, path/owner when returned, and metadata.
   - Read metadata for top results only when the search result lacks required table fields.
4. Render.
   - Sort by most recent first.
   - Use the recent files template in `output-format.md`.
   - Add useful observations after the table when supported by the data.

## Observation Guidance

Use short bullets with bold labels. Include only observations grounded in returned metadata:

- **High activity period:** peak times or clusters of edits.
- **Project focus areas:** repeated project/client/topic names across filenames.
- **Documentation types:** Docs, Sheets, Slides, PDFs, media, and other categories.
- **Notable pattern:** duplicates, working drafts, final exports, or repeated edits.
- **Client activity:** client-specific work when clear from names or metadata.
- **My Activity:** chronological narrative of the user's likely work only when ownership/editor metadata supports it.

## Large Result Sets

If the connector indicates 100+ files or a partial result, display the top 20 and note that additional files are not displayed. Suggest narrowing the timeframe or adding a project keyword.

## Stop Conditions

- Stop if recent-search capability is unavailable.
- Do not guess file activity from memory or prior conversation.
