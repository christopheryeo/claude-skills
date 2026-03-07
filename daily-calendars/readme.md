# Daily Calendars

Unified calendar skill that consolidates calendar operations into sub-commands.

## Sub-commands

- `search`: Natural-language Google Calendar search by date/time, title, attendee names, and attendee email/domain.
- `meeting`: Returns the default typical meeting definition, or validates whether a provided meeting matches it.

## Included resources

- `skill.md`: Main skill definition and workflow
- `scripts/search_calendar_helper.py`: Reference parsing and enrichment helpers copied from the former `search-calendar` skill, plus typical-meeting validation helpers

## Migration note

The standalone `search-calendar` workflow is now available under `daily-calendars` as the `search` sub-command.
