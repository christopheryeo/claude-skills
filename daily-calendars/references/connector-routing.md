# Connector Routing and Shared Calendar Rules

Read this reference before any sub-command that accesses Calendar data.

## Native Capability First

Use the connected native Google Calendar capability available in the current host. Select tools by their described operation rather than assuming one platform's tool name exists on another.

| Operation | Common Claude mappings | ChatGPT Work guidance |
|---|---|---|
| List accessible calendars | `list_gcal_calendars` or `gcal_list_calendars` | Use the connected Calendar operation that lists calendars, when exposed |
| List events in a range | `list_gcal_events` or `gcal_list_events` | Use the connected Calendar event-search/list operation |
| Read one event | `fetch_gcal_event` or `gcal_get_event` | Use the connected Calendar event-details operation |
| Check free/busy | `gcal_find_my_free_time` | Use native free/busy when exposed; otherwise derive availability from listed events |

Tool names can change between hosts. Match the capability description and required parameters. Do not call equivalent operations redundantly.

## Failure and Fallback Policy

If the native Calendar operation fails or is unavailable:

1. Stop the Calendar-dependent workflow and report the failed operation clearly.
2. In an interactive session, wait for Christopher's explicit approval before using Zapier or another non-native connector.
3. In a scheduled or unattended run, skip the operation and include the failure in the final report. Never auto-fallback.
4. Do not infer availability from email, prior conversation, or remembered calendar state.

Workspace instructions such as `CLAUDE.md` and `AGENTS.md` remain authoritative when they impose stricter rules.

## Time and Range Rules

- Resolve relative dates using the current date supplied by the host, not model memory.
- Default timezone: `Asia/Singapore` (`UTC+08:00`).
- Use explicit ISO 8601 boundaries whenever the connector supports them.
- Prefer half-open ranges: `start <= event < end`. For a day, query local midnight through the next local midnight.
- Preserve all-day events separately from timed events.
- Fetch only calendars and fields needed for the request.

## Read-Only Boundary

This skill may list calendars, search/list events, read event details, and inspect free/busy data. It must not create, update, move, accept, decline, or delete events.
