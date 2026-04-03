# Skill Architecture Policy — Native Connector First + Delegation Hierarchy

## Core Principle

Always build skills in two tiers:

1. **Fundamental skills** (e.g. `daily-emails`, `daily-calendars`, `daily-files`) — these are the single source of truth for their domain. They own the connector policy: **native connector first, Zapier/fallback second**. They own output formatting.

2. **Higher-order skills** (e.g. `daily-work`, `project-pulse-brief`, `customer-brief`) — these orchestrate across domains. They MUST delegate to the relevant fundamental skill rather than calling connectors directly.

## Why

Centralising connector policy in fundamental skills means that if a connector changes, you only update one place. It also ensures consistent output formatting everywhere.

## How to Apply

When building or reviewing any skill that touches Gmail, Google Calendar, or Google Drive, check:

| Domain | Fundamental skill | Higher-order skills must… |
|---|---|---|
| Gmail | `daily-emails` | Delegate all email read/search/draft operations |
| Google Calendar | `daily-calendars` | Delegate all event search/availability operations |
| Google Drive | `daily-files` | Delegate all browse/list/search/folder-prep operations |

### Rules

- Never let a higher-order skill call `gcal_*`, `gmail_*`, or `google_drive_*` tools directly for read/browse operations.
- Write operations (e.g. creating files, uploading) may still use Zapier Drive tools directly if the fundamental skill doesn't cover them.
- If a new connector domain is introduced, create a fundamental skill for it first, then have higher-order skills delegate to it.
