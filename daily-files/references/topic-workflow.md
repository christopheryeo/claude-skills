# Topic Workflow

Use this workflow to search Google Drive for files related to a topic or keyword and produce an executive briefing.

## Inputs

- `topic` is required: keywords, quoted phrases, acronyms, client names, project names, or initiative names.
- Optional filters: time range, file type, owner/collaborator, exclusions, viewed-by-me requirement.

Ask one short clarification if the topic is too broad or ambiguous to search responsibly.

## Steps

1. Confirm scope internally.
   - Identify the exact topic, likely synonyms, abbreviations, and alternate spellings.
   - Apply user-provided file type or time filters.
2. Construct Drive searches.
   - Use concise keyword queries. Search behavior may require every query token to match.
   - Use `special_filter_query_str` or equivalent for precise filters such as MIME type, modified time, owner, or `trashed = false`.
   - Start with the user's strongest keywords. If results are sparse, run one or two broader/alternate searches.
   - Default cap: 20 files.
3. Enrich top results.
   - Capture title, type, owner when returned, modified date, and link.
   - Fetch file content only when the user asks for content-level analysis or when the connector's best-effort fetch is appropriate and lightweight.
   - Generate <=60-word summaries focused on why each file appears relevant to the topic.
4. Group and prioritize.
   - Group by friendly type label when helpful: Docs, Sheets, Slides, PDFs, Folders, Other.
   - Prioritize by apparent relevance, recency, and exact project/client naming.
   - De-duplicate shortcuts, copies, exports, and repeated search hits when the connector returns enough metadata.
5. Render using the topic files template in `output-format.md`.

## File Type Filters

Use these MIME types when the connector supports Drive `q` filters:

- Docs: `application/vnd.google-apps.document`
- Sheets: `application/vnd.google-apps.spreadsheet`
- Slides: `application/vnd.google-apps.presentation`
- Folders: `application/vnd.google-apps.folder`
- PDFs: `application/pdf`

## Empty Results

Use this response:

```markdown
No Drive files matched `{topic}` with the current filters. Try alternative keywords, broaden the timeframe, or remove exclusions.
```

## Stop Conditions

- Stop if no topic can be inferred safely.
- Stop if Drive search capability is unavailable.
- Do not fabricate relevance or summarize unseen file content as if it was read.
