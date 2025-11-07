# Topic Files Skill Idea

## Mission
Enable Claude to retrieve and summarize Google Drive files related to a specified topic, giving users a consolidated view of all relevant documents, decks, and spreadsheets without manual searching.

## Why It Matters
- Reduces time spent hunting for topic-specific files across personal and shared drives.
- Surfaces hidden or forgotten artifacts that support research, planning, or execution.
- Improves collaboration by providing teammates with a curated packet of existing work on the topic.

## Primary Triggers
- "Find all files about [Topic] in Google Drive."
- "Pull Drive docs related to [Topic]."
- "Gather every presentation, doc, or sheet on [Topic]."

## Inputs & Data Sources
1. **Topic or Keyword Phrase**: Required user input that anchors all Drive queries.
2. **Google Drive API Search**: Full-text and metadata search scoped to accessible files, using keywords, titles, descriptions, and optionally file contents.
3. **Drive Labels & Shared Drives**: Optional filters to include/exclude specific drives, owners, or labels to narrow the result set.
4. **Recent Files Skill (Optional)**: Cross-reference recent Drive activity to highlight newly updated artifacts.

## Output Structure
1. **Topic Overview**: Short summary of the topic request and filters applied.
2. **Key Documents List**: Table grouping files by type (Docs, Sheets, Slides, PDFs) with titles, owners, last modified dates, and direct links.
3. **Highlights & Summaries**: Brief synopsis for each file using Claude's summarization, noting relevant sections or insights.
4. **Related Activity**: Optional section that surfaces recent edits or comments tied to the topic from Drive activity logs.
5. **Next Steps**: Suggested follow-up actions, such as requesting access, notifying collaborators, or compiling a briefing pack.

## Execution Notes
- Support advanced search operators (exact phrase, exclusions, owners) and expose them through optional parameters.
- Respect Drive permissions; clearly flag files where access must be requested.
- De-duplicate files that appear in multiple shared drives or shortcuts.
- Allow pagination or limits to avoid overwhelming the user with too many results.
- Cache topic queries when possible to speed up repeated lookups.

## Open Questions
- Should the skill integrate with Work-Day folder conventions when the topic relates to daily recon tasks?
- Do we need configurable relevance scoring (e.g., prioritize files with recent modifications or frequent collaboration)?
- Should summaries be stored for reuse, and if so, where should that cache live?
