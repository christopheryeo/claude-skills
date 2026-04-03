---
name: customer-brief
description: Generate a concise, executive-ready digest of internal touchpoints and external intelligence for a named customer.
---

# Customer Brief

Deliver an audit-friendly briefing that blends current relationship signals, open work, and market context so account teams are ready for any touchpoint.

## When to Use
- Pre-call preparation for account directors, CSMs, or executive sponsors.
- Requests such as "Run a customer brief for [Account]" or "What should I know before meeting [Account]?".

## Success Criteria
- 3–5 executive bullets with sentiment and next actions.
- ≤7 recent communications with channel, parties, action, and confidence score.
- ≤7 upcoming meetings normalized to the account timezone with prep notes.
- Deliverables rendered via the `list-files` skill output block, highlighting overdue items.
- ≥3 external insights (or explicit "No new items in last 14 days") with URLs and an audit trail of sources and keywords.

## Guardrails
- **Do:** Separate internal vs external signals, annotate owners/dates, log connectors and keywords.
- **Avoid:** CRM data, gated sources, or summarizing private chats without user-provided exports.
- Default research window: last 14 days (call out exceptions). Social scanning must stay public.
- Keep every section tight—use bullets, sentence fragments ≤30 words, and remove repeated phrasing to minimize token usage.

## Integration Policy

All email and calendar operations MUST be delegated to the appropriate unified skills. Do NOT call Gmail or Google Calendar tools directly.

| Need | Delegate to |
|---|---|
| Recent or topic-based email search | **daily-emails** `topic` sub-command (use account name as keyword) |
| Starred / priority emails for the account | **daily-emails** `starred` sub-command |
| Upcoming calendar meetings | **daily-calendars** `search` sub-command |
| Check meeting availability | **daily-calendars** `available` sub-command |

These skills own the connector policy (native first, Zapier fallback) and output formatting. This skill consumes their results.

## Fast Prep Checklist
1. Confirm account name/ID and primary timezone.
2. Verify access to tagged email folders, relevant calendars, shared drives, and trackers.
3. Align search plan (keywords, filters, priority sources) and sentiment rubric; start the audit log.

## Workflow
1. **Internal Communications** – Delegate to **daily-emails `topic`** using the account name as keyword (last 14 days). Consume the executive table output: date (account TZ), channel, participants, ≤40 word summary, sentiment + confidence, and required action. State fallback if empty.
2. **Upcoming Touchpoints** – Delegate to **daily-calendars `search`** for meetings involving the account team or customer stakeholders (next 14 days). Consume the results: normalize times to account timezone, list organizer, attendees, prep tasks, attachments, and flag critical sessions.
3. **Deliverables & Files** – Invoke `list-files` with the customer scope (folder/search query, limit ≤7, short summaries). Embed the returned `# 📁 DRIVE FILE LISTING` section as-is and note overdue statuses in follow-up bullets.
4. **Tasks/Trackers** – Import open items with owner, due date, status, blockers. If unavailable, log the gap and request updates.
5. **External Intel** – Run targeted web/news searches per plan. Capture up to five items with source, publish date, headline, and 1–2 sentence impact. Include search keywords, filters, and timestamp in audit log.
6. **Risks & Opportunities** – Distill recurring themes into Risks, Opportunities, Watchlist with owners and next steps. Highlight sentiment swings or repeated overdue work.
7. **Executive Summary & Audit Log** – Draft 3–5 bullets referencing supporting sections, maintain confident/empathetic tone, and append a concise audit log (sources, keywords, timestamps, manual overrides).

## Output Skeleton
```markdown
---
# Customer Brief: {{Account Name}}
*Generated: {{Local Timestamp}} | Primary Timezone: {{TZ}}*

## Executive Summary
- {{Insight + sentiment + action}}
- {{Insight}}
- {{Insight}}

## Recent Communications (Last 14 Days)
| Date ({{TZ}}) | Channel | Parties | Summary | Sentiment | Action |
| --- | --- | --- | --- | --- | --- |
| {{Sample row}} |

_Fallback_: "No new communications in last 14 days. Review archive label: {{Label}}."

## Upcoming Touchpoints
| Date | Time ({{TZ}}) | Meeting | Owner | Prep Notes |
| --- | --- | --- | --- | --- |
| {{Sample row}} |

{{Embed the `list-files` output here}}

## Risks & Opportunities
- **Risk:** {{Summary}} (Owner: {{Name}})
- **Opportunity:** {{Summary}} (Owner: {{Name}})
- **Watchlist:** {{Summary}} (Owner: {{Name}})

## External Highlights
1. _{{Source}}_ ({{Date}}) — {{Headline}} — {{Impact + action}} — [URL]
2. {{Additional items or "No new items in last 14 days."}}

## Search Log & Audit Notes
- Keywords: {{List}}
- Filters: {{Date range, types}}
- Sources Queried: {{List}}
- Exceptions: {{Access issues or manual inputs}}
```

## Quality Gate
- ≤7 rows per table unless user approves more.
- Every external item cites a working URL and date.
- Overdue/negative items flagged with owner follow-up.
- Audit log includes connectors, keywords, timestamps, and manual overrides.

## Validation Tips
- Smoke-test with active vs dormant accounts.
- Double-check timezone conversions on calendar entries.
- Ensure communications summaries stay ≤40 words and sentiment labels include confidence.
