# Set up Workday Skill Idea

## Mission
Orchestrate a stack of existing Claude skills to assemble everything needed to start the workday: surface overnight updates, plan priorities, gather required reference material, and stage working documents in Google Drive.

## Why It Matters
- Saves ramp-up time by consolidating updates, priorities, and resources into a single briefing.
- Reduces risk of missing urgent follow-ups by pulling highlights from email, calendar, and task tracking skills.
- Ensures the day's working folders, briefs, and checklists are ready before deep work begins.

## Primary Triggers
- "Set up my workday."
- "Kick off today using our standard morning stack."
- "Prepare everything I need for work this morning."

## Dependency Stack
1. **Morning Recon Brief Skill** – Summarize overnight news, inbox, and Slack pings relevant to the SNMG org. Accept the optional `include_email=false` flag when Recent Emails/Starred Email will be queried separately, so the recon brief can focus on macro context.
2. **Recent Emails Skill** – Surface unread or starred messages requiring follow-up, grouped by priority. Reuse its JSON payload directly rather than reformatting the same data in a custom parser.
3. **Starred Email Skill** – Provide context on high-priority threads and suggest next actions. Feed the thread IDs returned here back into Recent Emails when requesting deeper metadata to avoid duplicate API calls.
4. **Search Calendar Skill** – Pull today's meetings with agendas, prep docs, and participants. Support the `time_min/time_max` filters so the skill only queries the target workday window.
5. **Recent Files Skill** – Surface documents touched in the last 48 hours to resume in-progress work. Pass the normalized date from Reverse Date to keep the look-back window consistent with calendar queries.
6. **Work Day Skill** – Verify the Google Drive structure for the current date and create folders if missing. Invoke with the `dry_run=true` preview first so the orchestrator can decide whether to commit folder creation.
7. **Reverse Date & Reverse Month Skills** – Normalize user-specified dates for folder creation and timestamping. Cache their output for reuse by Work Day, Search Calendar, and Recent Files.

## Efficiency Opportunities Through Existing Skills
- **Minimize duplicate data fetching**: Run Morning Recon Brief first and inspect its payload for news or inbox highlights that already satisfy the kickoff brief requirements. Only call Recent Emails or Starred Email for deeper dives on threads flagged as urgent.
- **Pipeline shared identifiers**: Pass message IDs and calendar event IDs returned by upstream skills into downstream ones (e.g., Starred Email → Recent Emails, Search Calendar → Work Day) to avoid new lookup calls when assembling context.
- **Share normalized date objects**: Store the formatted date from Reverse Date/Month in orchestrator state so multiple skills consume the same value rather than recomputing formatting logic.
- **Leverage Work Day folder checks**: Defer all Drive structure validation to the existing Work Day skill instead of reproducing folder search/creation logic in this orchestration layer.
- **Reuse presentation components**: When generating the final kickoff brief, call the response templating utilities from Morning Recon Brief (if exposed) so the summary sections share styling and reduce redundant rendering code.

## Workflow Overview
1. **Determine Target Date**: Interpret the requested workday (default to today). Use Reverse Date/Month helpers to normalize formats.
2. **Collect Situation Report**: Run Morning Recon Brief, Recent Emails, and Starred Email to gather updates and urgent actions.
3. **Review Schedule**: Call Search Calendar to list today's meetings with prep requirements, adding links to meeting docs.
4. **Resume Context**: Use Recent Files to pull working documents and identify owners, status, and next steps.
5. **Prepare Workspace**: Invoke Work Day to ensure Drive folders exist, returning direct links for the day and month folders.
6. **Synthesize Plan**: Combine all collected data into a structured plan that highlights top priorities, blockers, and quick wins.
7. **Deliver Output**: Return a formatted morning kickoff brief with sections for priorities, schedule, follow-ups, and workspace links.

## Output Structure
- **Date & Focus Theme**
- **Top Priorities (3-5 bullets)**
- **Urgent Follow-ups** (linked to emails or Slack threads)
- **Today's Schedule Snapshot** (meetings, prep, logistics)
- **Active Docs & Resources** (recent files + Drive folder links)
- **Quick Wins / Administrative Tasks**
- **Notes & Reminders** (team shout-outs, approvals pending, etc.)

## Execution Notes
- Allow configuration toggles (e.g., skip email check on PTO days, focus on specific accounts).
- De-duplicate items appearing across multiple source skills; annotate with their origin for traceability.
- Respect data access scopes of each dependent skill; gracefully handle missing permissions with clear messaging.
- Cache Drive folder IDs when possible to reduce repeated search calls during the same session.
- Support follow-up actions like "Send me this summary" or "Create tasks for these follow-ups" via connected productivity tools.

## Open Questions
- Should the skill auto-schedule focus blocks based on free calendar windows?
- Do we need integration with task managers (e.g., Asana, Jira) to pull or push work items?
- What is the best format (Markdown vs. Notion page vs. email) for delivering the kickoff brief?
