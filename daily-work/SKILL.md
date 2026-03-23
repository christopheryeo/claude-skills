---
name: daily-work
description: >
  Full workday lifecycle with three sub-commands: START (morning enablement — email triage,
  calendar audit, Drive activity, news snapshot, workspace prep, executive brief; replaces
  set-up-workday), RECAP (end-of-day cross-reference of Calendar, Gmail, Drive, and all AI
  workforce Plans task logs into a comprehensive activity report in the work-day folder), and
  MINUTES (given a meeting title, find it in Calendar, search the work-day Drive folder for
  minutes, fall back to Gmail for transcript, then return a direct link). Use for
  "set up my workday", "start my day", "kick off today", "morning brief", "daily recap",
  "end of day", "wrap up the day", "what did I do today", "what happened today", "find the
  minutes", "meeting minutes for [title]", "where are the minutes", "get me the notes from
  [meeting]", "meeting transcript", or any workday activity review.
---

# Daily Work

A unified workday lifecycle skill that covers the full arc from morning activation to end-of-day synthesis, plus on-demand meeting minutes retrieval. It replaces the standalone `set-up-workday` skill by embedding the morning enablement workflow and adds an intelligent end-of-day recap that cross-references calendar, email, Drive, and AI workforce task logs. The MINUTES sub-command provides a fast path to locate and summarise meeting minutes or transcripts from Drive or email.

---

## Sub-Command Detection

| Trigger phrases | Sub-command |
|---|---|
| "set up my workday", "start my day", "kick off today", "morning brief", "prepare my morning", "morning package" | **start** |
| "daily recap", "end of day", "wrap up the day", "day summary", "recap my day", "what happened today", "what did I do today" | **recap** |
| "meeting minutes for [title]", "find the minutes", "where are the minutes", "get me the notes from [meeting]", "meeting transcript for [title]", "pull up the minutes" | **minutes** |

If the intent is ambiguous, ask which operation is intended. If the user says "work day" without further context, ask whether they want to set up the morning, run a recap, or find meeting minutes.

---

## Shared: Google Integration Tools

This skill uses the same tool integrations as the other daily skills:

### Gmail
- **gmail_search_messages** — search with Gmail query syntax
- **gmail_read_thread** — full thread context
- **gmail_read_message** — lightweight single-message details

### Google Calendar
- **list_gcal_calendars** / **list_gcal_events** / **fetch_gcal_event** — calendar retrieval

### Google Drive
- **google_drive_search** (builtin connector) — folder/file lookup
- **google_drive_find_a_file** (Zapier) — list files in a folder with metadata
- **google_drive_create_folder** (Zapier) — create folders for workspace setup
- **google_drive_create_file_from_text** (Zapier) — create files in Drive

### Timezone
- Default: **Singapore / GMT+8 (SGT)**
- All timestamps displayed as `HH:MM SGT` or `DD MMM YYYY, HH:MM SGT`

---

## Shared: SNMG18 Day-Folder Structure

Several sub-commands need the SNMG18 Working Docs day-folder. The structure is:

```
SNMG00 Management/
└── SNMG18 Working Docs/
    └── YYYY-MM Work/
        └── YYYY-MM-DD/
```

Before writing to or reading from the day-folder, verify it exists using the same folder lookup logic as the `daily-files` WORK-DAY sub-command: search for SNMG00 Management → SNMG18 Working Docs → month folder → day folder. Create missing month or day folders as needed. Cache folder IDs within the session to avoid repeated lookups.

---

## Shared: AI Workforce Team Members

The AI workforce consists of domain-specialist personas, each with their own workspace folder and Plans/ sub-folder:

| Member | Domain | Folder |
|--------|--------|--------|
| Vivien (PA) | Email, calendar, admin | `Vivien (PA)/Plans/` |
| Eddie (CFO) | Financial tasks | `Eddie (CFO)/Plans/` |
| Donny (Sales) | Sales-related | `Donny (Sales)/Plans/` |
| Mary (Marketing) | Marketing/collateral | `Mary (Marketing)/Plans/` |
| Cedric (Projects) | Project management | `Cedric (Projects)/Plans/` |
| Alex (Dev) | Development/technical | `Alex (Dev)/Plans/` |

Each Plans/ folder contains daily plan files named `YYYY-MM-DD-plans.md` and audit files named `YYYY-MM-DD Audit.md`.

---

## Sub-Command: START

**Purpose:** Execute the full morning enablement workflow — email triage, calendar audit, Drive activity review, news snapshot, workspace preparation, and executive brief synthesis. This replaces the standalone `set-up-workday` skill.

### Steps

1. **Normalize the target date.** Default to today. Convert to `YYYY-MM-DD` (reverse-date) and `YYYY-MM` (reverse-month) for consistent folder naming and query construction.

2. **Ensure workspace is ready.** Verify and create the SNMG18 Working Docs day-folder structure (month folder `YYYY-MM Work` and day folder `YYYY-MM-DD`). Cache folder IDs for later use.

3. **Pull unread email intelligence (last 48 hours).**
   - Query Gmail for all unread messages received in the last 48 hours.
   - For each message: capture sender, subject, received date/time, a 30-word summary, explicit expectations, deadlines, and a clickable Gmail URL.
   - If no unread emails: state "No unread emails in the last 48 hours."

4. **Audit today's calendar.**
   - Query Google Calendar for the current day (Asia/Singapore timezone).
   - For each event: start/end time (24-hour format), title, location, attendees, and a clickable calendar URL.
   - Flag conflicts or back-to-back meetings.
   - If empty: state "No calendar events scheduled for today."

5. **Review Drive file priorities (last 24 hours).**
   - Scan Google Drive for items modified in the last 24 hours, prioritizing the SNMG18 Meeting Minutes folder.
   - For each file: name, last modified timestamp, a 30-word summary, and a clickable link.
   - If no recent files: state "No recent file updates."

6. **Synthesize the What-I-Need-To-Do brief.**
   - Merge action items from unread emails, calendar prep requirements, and Drive follow-ups.
   - For each task: concise description, originating source with a clickable link, and any known due date.

7. **Capture a news snapshot.**
   - Surface two top international news stories and two top Singapore news stories.
   - Each: succinct headline, one-sentence context, and a source link.

8. **Compose the executive kickoff brief.** Deduplicate overlapping insights, prioritize urgent items, and format into these sections:

```markdown
# 🏢 WORKDAY BRIEF — DD Month YYYY

## Priorities & Quick Wins
[Urgent items from email, calendar, Drive — with source links]

## Urgent Follow-Ups
[Items requiring immediate attention]

## Today's Schedule
[Calendar events table with times, titles, attendees, prep flags]

## Workspace & Resources
[Day-folder status and links]

## What I Need To Do
[Merged action items with source, deadline, and links]

## News Snapshot
[2 international + 2 Singapore headlines with source links]

## Recommended Next Actions
[Prioritized suggestions for what to tackle first]
```

### Configurable Toggles

The user can opt out of specific components:
- `include_email` (default: true) — skip email triage
- `include_news` (default: true) — skip news snapshot
- `include_drive` (default: true) — skip Drive file review
- `focus_accounts` — scope to specific accounts or projects

Example: "Set up my workday, skip news" → runs everything except the news snapshot.

---

## Sub-Command: RECAP

**Purpose:** Build a comprehensive end-of-day activity report by cross-referencing Google Calendar, Gmail, Google Drive, and AI workforce Plans task logs. Produces a structured activity report stored in the Drive work-day folder.

### Steps

1. **Ensure the day-folder exists** using the shared folder verification logic.

2. **Query all four sources for today's activity:**

   **Calendar:**
   - Retrieve all events for today from Google Calendar.
   - For each: title, time, attendees, location, calendar link.
   - Exclude declined events and all-day "FYI" events (unless they have action items).

   **Gmail:**
   - Search for sent emails today: `in:sent newer_than:1d`
   - Search for starred emails today: `is:starred newer_than:1d`
   - For each: subject, recipients/sender, time, 30-word summary, Gmail link.
   - Apply token efficiency rules: max 10 per category, selective thread reading.

   **Drive:**
   - Search for files modified today: `modifiedTime > '{today_start_iso}'`
   - For each: filename, type, last modified time, 25-word summary, Drive link.
   - Exclude trashed files. Cap at 20 files.

   **AI Workforce Plans (all team members):**
   - For each team member in the AI Workforce table, locate their Plans/ folder.
   - Look for today's plan file (`YYYY-MM-DD-plans.md`) and audit file (`YYYY-MM-DD Audit.md`).
   - From the plans file: extract all tasks and their current status (🆕, 🔄, ✅, ❌, ⏭️).
   - From the audit file: extract completed task details, outputs, and verification results.
   - If a team member has no plans file for today, skip them silently.

3. **Compile the activity report** using this structure:

```markdown
# 📊 DAILY RECAP — DD Month YYYY

**Generated:** HH:MM SGT

---

## Meetings Attended

| # | Time | Title | Attendees | Minutes Available | Link |
|---|------|-------|-----------|-------------------|------|
| 1 | 10:00–11:00 | Weekly sync | Alice, Bob | ✅ [View](drive_link) | [📅 Event](cal_link) |
| 2 | 14:00–15:00 | Client review | Client team | ❌ Not found | [📅 Event](cal_link) |

## Emails Sent & Starred

| # | Time | Subject | To/From | Summary | Link |
|---|------|---------|---------|---------|------|
| 1 | 09:15 | Re: Contract terms | → Legal team | Sent revised terms | [📧 Open](gmail_link) |

## Files Created / Modified

| # | Time | File | Type | Summary | Link |
|---|------|------|------|---------|------|
| 1 | 11:30 | Q2 Roadmap.docx | 📄 Doc | New roadmap draft | [📁 Open](drive_link) |

## AI Workforce Task Activity

### Vivien (PA)
| # | Task | Status | Output |
|---|------|--------|--------|
| 1.1 | Draft BeeNext reply | ✅ Done | Email drafted and sent |

### Alex (Dev)
| # | Task | Status | Output |
|---|------|--------|--------|
| 2.1 | Update daily-work skill | ✅ Done | SKILL.md updated |

*(Only team members with today's plans are shown)*

---

## Day Summary

### Activity Overview
- **Meetings attended:** N (M hours total)
- **Emails sent/starred:** N
- **Files created/modified:** N
- **AI workforce tasks completed:** N of M across K team members

### Key Accomplishments
1. [Most significant outcome, with source link]
2. [Second most significant]
3. [Third most significant]

### Open Items & Follow-Ups
- [Action items that need attention tomorrow]
- [Incomplete AI workforce tasks to carry forward]

### Meetings Without Minutes
- [List of meetings where no minutes file was found in the day-folder]
```

4. **Check for meeting minutes.** For each calendar event in today's meetings, search the day-folder for a file whose name matches or contains the meeting title. Flag meetings with missing minutes in the "Meetings Without Minutes" section — this serves as a nudge to file them.

5. **Write the recap** to the Drive day-folder as `YYYY-MM-DD Daily Recap.md`.

6. **Present the recap to the user** as a clean executive summary. Focus on outcomes, accomplishments, and follow-ups rather than raw data.

### AI Workforce Plans Scanning

The recap scans Plans/ folders for all six AI workforce team members. The scanning approach:

1. **Locate each team member's folder** by searching Google Drive for the folder name (e.g., "Vivien (PA)").
2. **Look for today's files** inside their Plans/ sub-folder:
   - `YYYY-MM-DD-plans.md` — the task plan
   - `YYYY-MM-DD Audit.md` — execution audit trail
3. **Extract task data:**
   - From the plans file: task number, title, status icon, priority, effort estimate
   - From the audit file: action taken, output/deliverable, verification checklist
4. **Only include team members with activity.** If a team member has no plans file for today, omit them entirely from the output rather than showing an empty section.

This gives you a consolidated view of what the entire AI workforce accomplished during the day, not just your personal activity.

---

## Sub-Command: MINUTES

**Purpose:** Given a meeting title (or partial title), locate the meeting in Google Calendar, find the corresponding meeting minutes file in the work-day Drive folder, and if no minutes file is available, search Gmail for the meeting notes transcript. Return a direct link to what was found — no summary needed.

### Steps

1. **Find the meeting in Calendar.**
   - Search Google Calendar for events matching the provided title (fuzzy match — partial titles, abbreviations, and common variations should match).
   - Default to today's events. If no match found today, expand to the last 7 days.
   - If multiple matches: list them and ask the user to pick one.
   - If no match at all: inform the user and ask for a different title or date.
   - Capture: event date, time, title, attendees, calendar link.

2. **Determine the work-day folder** for the meeting's date.
   - Use the event date (not today's date, since the meeting may have been on a different day) to construct the day-folder path: `SNMG18 Working Docs / YYYY-MM Work / YYYY-MM-DD /`
   - Verify the folder exists. If it doesn't, note that no minutes have been filed and proceed to step 4 (email search).

3. **Search the day-folder for meeting minutes.**
   - List all files in the day-folder.
   - Look for files whose name contains the meeting title or recognisable keywords from it. Also match common patterns:
     - `[Meeting Title] Minutes`
     - `[Meeting Title] Notes`
     - `Minutes - [Meeting Title]`
     - `MOM - [Meeting Title]` (Minutes of Meeting)
     - Files containing the meeting title as a substring
   - Matching is case-insensitive and tolerant of minor variations (e.g., "Weekly Sync" matches "weekly-sync-minutes.docx").
   - **If a minutes file is found:** Return a direct link to the file. Go to step 5.
   - **If no minutes file is found:** Proceed to step 4.

4. **Fall back to Gmail for meeting transcript or notes.**
   - Search Gmail for messages related to the meeting:
     - Query: `subject:"{meeting title}" newer_than:7d` (broaden if the meeting was older)
     - Also try: `"{meeting title}" minutes OR notes OR transcript OR summary newer_than:7d`
   - Look for:
     - Emails with "minutes", "notes", "transcript", "summary", or "MOM" in the subject or body
     - Emails with attachments (which may contain the minutes as an attached document)
     - Automated meeting transcript emails (from Google Meet, Otter.ai, Fireflies.ai, etc.)
   - If found: return a direct link to the most relevant email. Do not read the content or generate a summary.
   - If nothing found in email either: report that no minutes or transcript could be located.

5. **Present the result.**

   **When minutes are found (Drive):**
   ```markdown
   📄 **Meeting Minutes:** [Meeting Title] — DD MMM YYYY
   [📄 Open minutes in Drive](drive_link) | [📅 View calendar event](calendar_link)
   ```

   **When transcript is found (Gmail):**
   ```markdown
   📧 **Meeting Transcript:** [Meeting Title] — DD MMM YYYY
   [📧 Open transcript in Gmail](gmail_link) | [📅 View calendar event](calendar_link)
   ```

   **When nothing is found:**
   ```markdown
   ⚠️ **No minutes or transcript found for "[Meeting Title]"**

   **Meeting:** [Full title] | **Date:** DD MMM YYYY, HH:MM–HH:MM SGT
   **Attendees:** [Names]
   **Calendar event:** [📅 View](calendar_link)

   **Searched:**
   - ❌ Drive day-folder: `YYYY-MM-DD/` — no matching files
   - ❌ Gmail: no matching emails with minutes, notes, or transcript

   Would you like me to search with different keywords, or check a different date?
   ```

### Search Broadening

If the initial search doesn't find results, the skill progressively broadens:
1. First: exact title match in the day-folder
2. Then: partial/keyword match in the day-folder
3. Then: Gmail subject search with the full title
4. Then: Gmail full-text search with title keywords + "minutes OR notes OR transcript"
5. If all fail: report not found and offer alternative search terms

---

## Guard Rails

- Never fabricate activity data, timestamps, or links — use only API data.
- RECAP produces a point-in-time snapshot; running it multiple times in a day is safe and each run captures the latest state.
- Respect timezone preferences — default Singapore / GMT+8.
- If any integration fails, explain clearly and continue with available data.
- Keep summaries neutral and derived from actual data.
- Cache folder IDs, message IDs, and event IDs within the session to prevent repeated lookups.
- All source links must be real — Gmail links from message IDs, Calendar links from event data, Drive links from file metadata.
- MINUTES never modifies files — it is read-only. It finds and returns a direct link, nothing else.

### Quality Checklist (before finalizing any output)

Sequential numbering ✅, working links from API data ✅, timezone stated ✅, summaries within word limits ✅, deduplication applied (RECAP) ✅, timestamps current ✅.

---

## Relationship to Other Skills

This skill **replaces** `set-up-workday` — the START sub-command provides the same morning enablement workflow.

This skill **complements** (does not replace):
- **daily-plans** — Plans track what you *intend* to do; RECAP tracks what *actually happened* and pulls in task completion data from all AI workforce members' Plans folders.
- **daily-files** — The WORK-DAY sub-command in daily-files creates Drive folder structure. This skill reuses that folder logic but adds activity tracking and minutes retrieval on top.
- **daily-emails** — This skill queries Gmail for RECAP and MINUTES but doesn't replace daily-emails' full sub-command suite (drafting, responding, proposing).
- **daily-calendars** — This skill reads calendar data but doesn't replace search, availability checking, or meeting validation.
- **daily-journals** — Journals are free-form reflections; RECAP is structured activity tracking. Both can coexist.

---

## Edge Cases

- **RECAP finds zero activity:** Report a quiet day. Don't fabricate entries.
- **RECAP runs mid-day:** Works fine — captures everything up to the current moment. Can be run again later.
- **Multiple recaps in one day:** Each run overwrites the recap file with the latest data. The recap is a snapshot, not an append log.
- **Calendar event was declined:** Exclude from RECAP unless it has a minutes file in the day-folder (meaning the user may have attended despite declining).
- **MINUTES: meeting was on a different day:** The skill uses the calendar event's date, not today, to find the correct day-folder.
- **MINUTES: meeting title is very generic (e.g., "Sync"):** If multiple matches, list them with dates and attendees so the user can pick the right one.
- **MINUTES: transcript email has an attachment:** Note the attachment filename and provide the email link so the user can download it.
- **AI workforce member folder not found in Drive:** Skip that member silently — they may not have a folder set up yet.
- **Plans file exists but audit file doesn't:** Show tasks from the plans file with their current status. Note that no audit trail is available.
