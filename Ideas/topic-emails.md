# Topic Emails Skill Idea

## Opportunity
- Users frequently need to gather all Gmail correspondence on a specific subject for reporting or follow-up but must run multiple manual searches.
- Existing skills focus on summarizing recent emails or drafting responses rather than curating topic-centric threads.
- Centralized retrieval of topic-related messages would accelerate knowledge gathering for briefings, proposals, and audits.

## Proposed Solution
1. Add a new `topic-emails/skill.md` describing the automation workflow and configuration knobs.
2. Accept inputs for `topic`, optional `time_range` filters, and Gmail label exclusions to limit noise.
3. Use Gmail search operators (`subject:`, quoted phrases, `after:`, `before:`) to build a precise query covering threads and single messages.
4. Retrieve matching threads via the Gmail API, expanding to include message metadata (participants, dates) and snippets for quick triage.
5. De-duplicate results by thread ID and sort chronologically or by relevance to surface the most actionable messages first.
6. Provide structured output sections:
   - Summary of total matches and key correspondents.
   - Highlight of top 3 emails (subject, sender, date, snippet, link).
   - Full list of remaining emails with direct Gmail URLs and thread context notes.
7. Support optional export formats (Markdown list, CSV attachment) for downstream briefing documents.
8. Document authentication requirements, rate limit handling, and graceful messaging when no emails match the topic.

## Example Usage
- **Input:** `topic = "Q3 roadmap"`, `time_range = last 60 days`, `exclude_labels = ["Promotions"]`.
- **Output:**
  - 18 emails found across 7 threads.
  - Key correspondents: Product Leadership, Regional PMs, Marketing Ops.
  - Top matches include kickoff invite, feedback summary, and final approval thread with direct links.

## Expected Impact
- Reduces time spent manually searching Gmail by aggregating topic-relevant emails in seconds.
- Improves preparation for meetings, briefs, and audits through comprehensive visibility of related correspondence.
- Enables teams to capture institutional knowledge and follow-up tasks tied to specific initiatives or clients.
