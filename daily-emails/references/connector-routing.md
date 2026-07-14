# Connector Routing and Shared Gmail Rules

Read this reference before any sub-command that accesses Gmail.

## Shared: Gmail Capability Routing

### Connector Policy

Use the connected native Gmail capability available in the current host. Select tools by their described operation, not by assuming that one platform's tool name exists on another.

| Operation | Common Claude mapping | Common ChatGPT Work mapping |
|---|---|---|
| Search messages | `gmail_search_messages` | `gmail_search_emails` |
| Read full thread | `gmail_read_thread` | `gmail_read_email_thread` |
| Read single message | `gmail_read_message` | `gmail_read_email` |
| Create draft reply | `gmail_create_draft` or `gmail_create_draft_reply` | `gmail_create_draft` with `reply_message_id` |
| List drafts | `gmail_list_drafts` | `gmail_list_drafts` |

> **Rule:** Use only the native connected Gmail capability. If it returns an error or is unavailable:
> 1. **STOP.** Do not silently retry through Zapier or another connector.
> 2. **Interactive sessions:** Report the unavailable operation and error. Wait for Christopher's explicit approval before using any non-native fallback.
> 3. **Scheduled/unattended runs:** Skip the operation and surface the failure in the end-of-run report. Never auto-fallback.
> 4. Never call equivalent connectors redundantly in the same request.
>
> Repository or workspace instructions such as `CLAUDE.md` and `AGENTS.md` remain authoritative when they impose stricter connector rules.

## Shared: Query Construction

All retrieval sub-commands build Gmail queries using these patterns:

- **Time (relative):** `newer_than:1d`, `newer_than:7d`, `newer_than:24h`
- **Time (absolute):** `after:YYYY/MM/DD`, `before:YYYY/MM/DD`
- **Folder:** `in:inbox`, `in:sent`, `in:drafts`, `is:starred`
- **Participants:** `from:email`, `to:email`, `cc:email`
- **Content:** `subject:"phrase"`, `"exact match"`, `label:name`
- **Exclusions:** `-category:promotions`, `-from:noreply`, `-subject:unsubscribe`
- **Combine with:** `OR`, `AND`, parentheses for grouping

## Shared: Token Efficiency Rules

These apply to ALL retrieval sub-commands:

1. **Result limits:** Max 10 results per search category, 40 total max per invocation
2. **Selective thread reading:**
   - Priority 1: Unread + Starred → use the full-thread read capability
   - Priority 2: Starred only → use the full-thread read capability
   - Priority 3: Unread only → use the full-thread read capability
   - Priority 4: Everything else → use the single-message read capability
   - If total emails < 15, read all threads fully
   - Never read more than 5 full threads in a single execution
3. **Monitor token usage:** If approaching limits, stop fetching and present available data
4. **Inform user:** If results are truncated, state this and suggest narrower searches
