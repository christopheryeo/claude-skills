# Typical Meeting Profile

Use this reference for the `meeting` sub-command.

A typical meeting is:

- exactly 60 minutes;
- online;
- hosted with a Google Meet link.

## Behavior

- When the user asks for the definition, return only the concise three-bullet definition.
- When the user supplies a meeting to validate, evaluate all three conditions and output only `yes` when every condition passes; otherwise output only `no`.
- A `meet.google.com` URL or explicit Google Meet conference metadata satisfies the Google Meet condition.
- Do not access Calendar when the supplied details are sufficient for validation.
