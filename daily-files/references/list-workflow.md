# List Workflow

Use this workflow for listing all direct children inside a named Google Drive folder.

## Inputs

- Folder name, folder URL, or folder ID.
- Optional parent folder context if the user supplies a hierarchy.

## Steps

1. Resolve the target folder.
   - If the user provided a Drive folder URL or folder ID, use it directly with metadata lookup to confirm it is a folder.
   - If the user provided a name, search Drive for that name with a folder MIME-type filter and `trashed = false`.
   - If the user supplied a parent context, search within that parent using `'{parent_id}' in parents`.
2. Handle ambiguity.
   - If multiple folders plausibly match, present the folder names, paths/parents when available, modified dates, and links; ask the user to choose.
   - If no folder matches, say no folder with that name was found and suggest a shorter or alternate folder name.
3. List direct folder children.
   - Use the native Drive folder-list operation with the folder URL or ID format required by the connector.
   - Request up to 100 direct children when the connector supports a limit. If the result may be partial, state that.
   - Do not recursively list subfolders unless the user asks.
4. Enrich each item.
   - Map MIME type to a friendly type label using `output-format.md`.
   - Convert timestamps to the selected timezone.
   - Generate a <=25-word summary from file name, type, and returned metadata. Fetch file contents only if the user asks for content-level summaries.
5. Sort and render.
   - Sort by last modified descending when modification timestamps are available.
   - Number sequentially starting from 1.
   - Use the folder contents template in `output-format.md`.

## Additional Sections

Include only when data supports them:

- **Notable Items:** very recent edits, obvious shared/client items, or large files when size is returned.
- **File Type Breakdown:** count by friendly type when the folder has 5+ items.
- **Subfolders:** short separate table for folder children.

## Stop Conditions

- Stop if the folder cannot be uniquely resolved.
- Stop if the Drive folder-list capability is unavailable.
- Never list from local filesystem paths as a substitute for Drive folders.
