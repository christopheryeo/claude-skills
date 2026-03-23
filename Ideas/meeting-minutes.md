# Meeting Minutes Skill Idea

## Mission
Provide a single command that gathers all reference material for a specified meeting date by orchestrating calendar, Workday drive, and email skills, enabling fast compilation of accurate meeting minutes.

## Why It Matters
- Eliminates manual searching across calendar, drive, and email to find relevant meeting artifacts.
- Ensures meeting minutes are comprehensive by combining agendas, notes, and transcripts from multiple systems.
- Speeds up post-meeting documentation and distribution, improving accountability and follow-up.

## Primary Triggers
- "Prepare meeting minutes for [Date]."
- "Compile all materials for meetings on [Date]."
- "Summarize meetings held on [Date] with transcripts and documents."

## Inputs & Data Sources
1. **Date Parameter**: User-specified meeting date that anchors all lookups.
2. **Search Calendar Skill**: Query calendar events on the given date to identify meetings, participants, and time blocks.
3. **Workday Drive (Workday Folder)**: Use Workday skills to retrieve meeting minutes or related documents stored for that work day.
4. **Email (Subject: "Meeting Records")**: Scan inbox for emails with matching subject on or near the target date to capture transcripts or automated notes.

## Output Structure
1. **Meeting Overview**: List of meetings with titles, times, attendees, and calendar links.
2. **Attached Documents Summary**: For each meeting, reference minutes or files discovered in the Workday folder with access paths.
3. **Email Transcript Highlights**: Summaries or excerpts from emails labeled "Meeting Records" relevant to the date.
4. **Action Items & Decisions**: Extracted follow-ups based on documents and transcripts, organized by owner and due date when available.
5. **Outstanding Gaps**: Identify meetings lacking artifacts so the user can request additional input.

## Execution Notes
- Accept both natural language dates ("last Tuesday") and ISO formats, normalizing them before searches.
- De-duplicate meetings when calendar, drive, and email records refer to the same session.
- Preserve source citations or links for every extracted artifact so users can verify details quickly.
- Allow optional filters (e.g., specific team, organizer) to narrow results for busy meeting days.
- Provide a ready-to-share Markdown or docx output that can be sent to stakeholders.

## Open Questions
- Should the skill automatically create a follow-up task list in Workday or task management tools?
- Do we need to handle multi-day events differently when collecting artifacts?
