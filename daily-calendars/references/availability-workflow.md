# Availability Workflow

Use this reference for the `available` sub-command.

## Required Inputs and Defaults

Resolve:

- requested date and start time;
- duration, defaulting to the typical meeting duration of 60 minutes when omitted;
- meeting mode: physical or online. If omitted, use the typical meeting mode of online;
- timezone, defaulting to `Asia/Singapore`.

Ask a short clarification when the date or start time is genuinely missing. Ask whether a meeting is physical only when that classification affects the answer and cannot be inferred safely.

## Availability Rules

Apply these rules in order:

1. **Weekdays only:** Monday through Friday.
2. **Working hours:** the entire meeting must fit between 10:00 AM and 6:00 PM.
3. **Lunch:** the meeting must not overlap 12:00 PM through 2:00 PM.
4. **Calendar conflicts:** the meeting must not overlap a busy event. Cancelled or declined events are not busy; treat tentative events as busy unless Christopher says otherwise.
5. **Thirty-minute buffers:** require at least 30 minutes between the requested meeting and the nearest busy timed event on both sides.
6. **One physical meeting per day:** a requested physical meeting is unavailable when another confirmed physical meeting already exists that day.

Use native free/busy data when available. Otherwise list all relevant events for the day and derive busy intervals. Ignore working-location markers, but treat out-of-office and other blocking all-day events as unavailable unless the connector marks them free.

## Physical Meeting Classification

Classify an event as physical only when all are true:

- It has a credible real-world location such as a street address, building, venue, room, or city.
- It has no Google Meet, Zoom, Microsoft Teams, Webex, or other online-conference link in conference metadata, location, or description.
- Its location is not empty, a URL, or a virtual indicator such as `online`, `virtual`, `remote`, `zoom`, `google meet`, `meet`, `teams`, `webex`, `phone`, `call`, `dial-in`, `tbd`, or `tba`.
- Its title and description do not identify it as a call, video call, virtual, online, or remote meeting without a corresponding physical venue.

If the evidence is ambiguous, do not count it as physical automatically. Ask Christopher to confirm when the classification changes the result.

Sentient has no physical office. Never suggest a Sentient office as a venue.

## Evaluation Procedure

1. Validate weekday, working hours, and lunch before reading Calendar when those rules alone decide the answer.
2. Query the requested day when Calendar evidence is required.
3. Normalize busy intervals into the requested timezone.
4. Check overlap and the 30-minute buffers against both the previous and next busy intervals.
5. Apply the physical-meeting rule when relevant.
6. Return a clear yes/no result with evidence.

When unavailable, find the nearest valid alternative only when requested. Search chronologically during the next ten weekdays, preserving duration and mode. Do not claim an alternative is free until Calendar data verifies it.

## Stop Conditions

- If Calendar capability is unavailable, say availability cannot be verified and stop.
- If only partial Calendar data is returned, report that limitation and do not give an unqualified `YES`.
- This workflow never creates or changes an event.
