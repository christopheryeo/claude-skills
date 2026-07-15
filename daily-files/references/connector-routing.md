# Connector Routing and Shared Drive Rules

Read this reference before any sub-command that accesses Google Drive.

## Native Capability First

Use the connected native Google Drive capability available in the current host. Select tools by their described operation rather than assuming one platform's tool name exists on another.

| Operation | Legacy mapping category | ChatGPT Work guidance |
|---|---|---|
| Search files/folders | Drive search | Use the connected Drive search operation with concise keywords and Drive `q` filters when available |
| List folder children | Folder listing | Use the connected Drive folder-list operation for direct children |
| Read metadata | File/folder lookup | Use the connected Drive metadata operation for exact file/folder details |
| Create folders | Folder creation | Use the connected Drive create-folder operation only for the `work-day` workflow |

Tool names can change between hosts. Match the capability description and required parameters. Do not call equivalent operations redundantly.

## ChatGPT Google Drive Connector Hints

- Search: use concise `query` terms plus `special_filter_query_str` for precise Drive filters.
- Folder search filter: `mimeType = 'application/vnd.google-apps.folder' and trashed = false`.
- Parent filter: `'{parent_id}' in parents`.
- Recent filter: `modifiedTime > '{iso_timestamp}' and trashed = false`.
- Exclude folders from file searches when appropriate: `mimeType != 'application/vnd.google-apps.folder'`.
- List folder: pass a Drive folder URL or the literal `root`; do not pass a raw folder name to folder-list operations.
- Create folder: pass the parent folder ID, folder URL, or `root` according to the connector schema.

## Failure and Fallback Policy

If the native Drive operation fails or is unavailable:

1. Stop the Drive-dependent workflow and report the failed operation clearly.
2. In an interactive session, wait for Christopher's explicit approval before using Zapier or another non-native connector.
3. In a scheduled or unattended run, skip the operation and include the failure in the final report. Never auto-fallback.
4. Do not infer Drive state from email, prior conversation, remembered file names, or local filesystem files.

Workspace instructions such as `CLAUDE.md` and `AGENTS.md` remain authoritative when they impose stricter rules.

## Time and Search Rules

- Resolve relative dates using the current date supplied by the host, not model memory.
- Default timezone: `Asia/Singapore` (`UTC+08:00`).
- Use explicit ISO 8601 timestamps whenever the connector supports time filters.
- Keep search queries short and keyword-focused; Drive keyword search can behave like AND matching.
- Use alternate searches for abbreviations, synonyms, and project names when a first topic search has low recall.
- Fetch only files, folders, and fields needed for the request.

## Read and Write Boundary

This skill may search Drive, list direct folder children, read metadata, fetch file content when needed for summaries, and create folders for the `work-day` workflow. It must not delete, move, rename, share, upload, or modify file contents.
