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
1. **Morning Recon Brief Skill** – Summarize overnight news, inbox, and Slack pings relevant to the SNMG org.
2. **Recent Emails Skill** – Surface unread or starred messages requiring follow-up, grouped by priority.
3. **Starred Email Skill** – Provide context on high-priority threads and suggest next actions.
4. **Search Calendar Skill** – Pull today's meetings with agendas, prep docs, and participants.
5. **Recent Files Skill** – Surface documents touched in the last 48 hours to resume in-progress work.
6. **Work Day Skill** – Verify the Google Drive structure for the current date and create folders if missing.
7. **Reverse Date & Reverse Month Skills** – Normalize user-specified dates for folder creation and timestamping.

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
