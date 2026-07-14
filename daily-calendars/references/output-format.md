# Calendar Output Format

Use concise executive formatting. Show only fields that help answer the request.

## Search Results

Start with the coverage period and timezone, then use:

| # | Date | Time | Event | Attendees | My RSVP | Location / Join | Prep |
|---:|---|---|---|---|---|---|---|

Rules:

- Link the event title when the connector supplies a real event URL.
- Use local date and time, not raw ISO strings, in the visible table.
- Use `All day` for all-day events.
- Use `None` or omit the field when attendee data is unavailable; do not invent it.
- Display `accepted`, `tentative`, `needs action`, `declined`, or `organizer` for `My RSVP` when known.
- Mark prep with `Yes` or `No`.
- Sort chronologically and number rows continuously.

After the table, include only useful sections such as:

- **Conflicts:** overlapping accepted/tentative events.
- **Preparation:** events with concrete prep indicators.
- **Coverage:** truncation, partial data, or calendars not searched.

## Availability Result

When available:

```text
YES - [date, start-end, timezone] is available.
Context: [calendar and rule evidence]
Nearest conflicts: [previous/next event or none]
```

When unavailable:

```text
NO - [date, start-end, timezone] is unavailable.
Reason: [weekday / working hours / lunch / conflict / buffer / physical-meeting rule]
Conflicting event: [linked title and time, when applicable]
Nearest verified slot: [date and time, only when requested and verified]
```

When Calendar cannot be checked:

```text
I cannot verify availability because the connected Calendar capability is unavailable. No event was created or changed.
```

## No Results

State the timeframe and filters used. Offer one useful narrowing or broadening option without claiming there are no events outside the searched scope.
