# Integrated Project Pulse Brief

## Concept
Create a "Project Pulse Brief" skill that assembles a concise status report for a focus project or client by stacking existing data-gathering skills. The brief summarizes the latest conversations, meetings, files, and relevant news so stakeholders can get up to speed quickly.

## Building Blocks to Stack
- **Email signals** from `recent-emails/skill.md` to capture the newest inbound, outbound, or starred threads tied to the project, using their chronological narrative and metadata outputs.
- **Calendar context** from `search-calendar/skill.md` to surface past and upcoming meetings, attendees, and agendas related to the project timeline.
- **Work artifacts** from `recent-files/skill.md` to list modified Google Drive documents, decks, or spreadsheets that indicate current progress.
- **External developments** from `news-snapshot/skill.md` to add market or industry headlines that might impact the project's strategy.

## Proposed Workflow
1. Accept inputs like project or client name, date range, and optional keyword filters.
2. Invoke `recent-emails` and `recent-files` in parallel, filtering for the project keywords and compiling key takeaways plus direct links.
3. Call `search-calendar` to extract relevant meetings, noting objectives, participants, and action items.
4. Pull targeted industry stories via `news-snapshot` to frame external context.
5. Synthesize the collected data into a layered brief with sections for executive summary, communications, meetings, deliverables, and external signals. Include follow-up prompts and unanswered questions surfaced by the stacked skills.

## Why It’s Valuable
- Delivers a single narrative assembled from multiple authoritative sources already present in the library.
- Reduces manual cross-referencing across email, calendar, Drive, and news feeds.
- Provides a reusable template for weekly project reviews, client updates, or onboarding new collaborators.
