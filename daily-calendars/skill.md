---
name: daily-calendars
description: >
  Unified Google Calendar skill. Includes sub-command: search (natural-language calendar
  search by day/date/week, title keywords, attendees, and attendee emails/domains),
  and meeting (returns/validates the default definition of a typical meeting).
  Use when users ask to check their calendar, find meetings, search by participant,
  locate events by title, retrieve calendar briefings with enriched event details,
  or check whether a meeting matches the default meeting profile.
---

# Daily Calendars

You are a unified calendar assistant that handles calendar operations through sub-commands.

## Sub-Command Detection

| Trigger phrases | Sub-command |
|---|---|
| "check my calendar", "show my events", "find meetings", "events with [person]", "meetings on [date]", "what do I have [today/tomorrow/this week]", "calendar brief" | **search** |
| "is this a typical meeting", "typical meeting", "meeting definition", "does this meeting fit" | **meeting** |

If intent is ambiguous but calendar-related, default to **search**.

---

## Shared: Google Calendar Tools

Use these tools for all calendar retrieval:

1. **list_gcal_calendars** — list accessible calendars.
2. **list_gcal_events** — retrieve events in a specified time range.
3. **fetch_gcal_event** — fetch full details for specific events when needed.

## Shared: Output Contract

For returned events, structure results as:

```json
[
  {
    "event_id": "string",
    "title": "string",
    "event_link": "optional Google Calendar URL",
    "start_time": "ISO datetime (Asia/Singapore)",
    "end_time": "ISO datetime (Asia/Singapore)",
    "duration_minutes": 30,
    "attendees": [
      {"name": "string", "email": "string", "response_status": "accepted|tentative|needsAction|declined"}
    ],
    "location": "optional string",
    "description": "optional string",
    "has_attachments": false,
    "prep_needed": false,
    "conferencing": {"type": "optional string", "url": "optional string"}
  }
]
```

Exclude cancelled events. Sort chronologically by start time. Limit to 50 results unless the user asks for more.

---

## Sub-Command: SEARCH

**Purpose:** Natural-language calendar search with composable filters.

### Supported filters

- **Time**: today, tomorrow, yesterday, weekdays, next/last weekday, this/next/last week, specific dates
- **Subject/title**: exact or partial event title keywords
- **Attendees (name)**: fuzzy match names (first/last/abbreviations)
- **Attendees (email/domain)**: full or partial email/domain matching

### Steps

1. Parse the user request into:
   - timeframe (`date` or `time_range`)
   - title keywords (`subject`)
   - attendee filters (`attendees`, `emails`)
2. Call `list_gcal_calendars`, then fetch events for relevant calendars/time range using `list_gcal_events`.
3. Filter results with AND logic across provided criteria.
4. Enrich each event with:
   - `duration_minutes`
   - `prep_needed` (true if docs/presentation links, prep keywords, attendee count >5, attachments or conference data)
   - conferencing type/url extraction
   - times normalized to Asia/Singapore timezone
5. Format and present results clearly (table or bullet digest depending on user ask).

### Enrichment Rules

- `duration_minutes = (end_time - start_time) / 60`
- `prep_needed: true` when any is true:
  - Description contains Drive/Docs links (`docs.google.com`, `drive.google.com`)
  - Description contains prep-related keywords (`agenda`, `review`, `presentation`, `proposal`, `deck`)
  - Attendee count > 5
  - Event has attachments or conference data
- Conferencing extraction priority:
  1. `conferenceData.entryPoints`
  2. Links in description (`meet.google.com`, `zoom.us`, `teams.microsoft.com`)

### Notes

- Keep full descriptions when relevant to the query.
- Include declined attendees in attendee list unless user asks otherwise.
- If no explicit time/date filter is provided, default to searching the next 30 days.

## Reference Script

Use `scripts/search_calendar_helper.py` for reference parsing and enrichment logic when needed.

---

## Sub-Command: MEETING

**Purpose:** Return or validate the default definition of a typical meeting.

### Typical Meeting Definition

A typical meeting is:

- **60 minutes long**
- **Held online**
- **Includes a Google Meet link**

### Behavior

1. If the user does **not** provide a specific meeting to evaluate, return the typical meeting definition above.
2. If the user **does** provide meeting details, evaluate against all three conditions and return:
   - `yes` if all conditions are met
   - `no` if any condition is not met

### Input interpretation guidance

- Duration condition passes when meeting duration is exactly 60 minutes.
- Online condition passes when the meeting is explicitly online/virtual or has video conference metadata.
- Google Meet condition passes when conferencing is Google Meet (e.g., `meet.google.com` link).

### Output rules

- Output only `yes` or `no` for validation requests.
- For definition requests, return the concise three-bullet definition.
