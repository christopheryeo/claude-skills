---
name: prospect-brief
description: Generate an executive briefing on a single lead or sales prospect, covering the last 60 days of emails, Google Drive files (including meeting minutes), Google Calendar meetings, and the matching entry in Mary's Lead Gen Log or Donny's Sales Prospects Tracker. Use when Christopher says "brief me on [company/person]", "prospect brief for [X]", "lead brief", "what's happening with [prospect]", or "prep me on [lead]".
---

# Prospect Brief

Deliver a tight, executive-ready briefing on one lead or prospect by pulling together every internal touchpoint from the last 60 days plus the relevant sales/lead tracker entry. Output is rendered in chat only — nothing is saved.

## When to Use
- "Brief me on [Acme Corp]" / "prospect brief for [Jane Tan]" / "lead brief for [domain]".
- Pre-call or pre-meeting prep on a specific lead or prospect.
- Do NOT use for existing customers/accounts (use `customer-brief`) or for whole-pipeline reviews.

## Inputs
- **Identifier** — accept any of: company name, person name, or email / email domain. Christopher may give one or several. Use all provided identifiers as search keywords across every source.
- **Window** — fixed at **last 60 days** unless Christopher overrides.

## Scope — Match Wide, Filter Narrow (deal-relevance wins)
Identifier-matching finds everything involving the company/contact — but "same company/people" ≠ "about this deal." The brief is about **one specific opportunity**, not the whole relationship.

1. **Match wide** to gather candidates (all emails/files/meetings touching any identifier).
2. **Filter narrow** by deal relevance. Build a **deal fingerprint** from the tracker entry: product name, agent names, commercial keywords, and reference codes (e.g. Carbon Amber, back-office, AP/expense, Xero, "proposal R#", `Sen-LVNS-…`). A candidate is **on-deal** only if its subject/content/attendees map to that fingerprint.
3. **On-deal** items go in the main tables. **Entity-matched but off-topic** items (loan-repayment threads, portfolio/relationship meetings, unrelated introductions) go in a separate **Adjacent** list — one line each, visible but never counted as deal momentum.
4. **Deal-topic relevance is authoritative over the tracker log.** If the tracker logged a touchpoint under this prospect but its actual purpose was off-topic (e.g. a relationship meeting where the pilot was only briefly mentioned), it belongs in **Adjacent**, not the main brief — note the tracker cross-reference so nothing looks dropped.
5. Do **not** widen matching to catch more (e.g. a bare `@domain` calendar sweep) — that pulls in more off-deal noise. Widen the net only to find candidates, then let the deal fingerprint decide.

## Log Source — Auto-Detect by Folder
Determine which tracker to brief from based on the currently selected workspace folder:

| Selected folder context | Primary tracker |
|---|---|
| `Mary (Marketing)/` | **Lead Gen Log** — `Mary (Marketing)/Knowledge/Lead Gen Log.md` |
| `Donny (Sales)/` | **Sales Prospects Tracker** — `Donny (Sales)/Knowledge/Sales Prospects Tracker.md` |
| Root / ambiguous / neither | Search **both** trackers; label which one(s) the match came from |

If the auto-detected tracker has no match but the other does, fall back to the other and note the cross-reference (a lead may have graduated from Mary's log to Donny's tracker — surface both if found).

## Connector Policy — Native Only (per CLAUDE.md)
All email, calendar, and Drive operations go through the unified skills, which are bound to native MCP connectors. **Never call Zapier-routed tools.** If a native call fails, report it and stop — do not fall back to Zapier.

| Need | Delegate to |
|---|---|
| Emails to/from the lead (last 60 days) | **daily-emails** `topic` sub-command (identifier as keyword) |
| Drive files incl. meeting minutes | **daily-files** `topic` sub-command (identifier as keyword) |
| Meetings with the lead (past 60 days) | **daily-calendars** `search` sub-command |

Trackers (`Lead Gen Log.md` / `Sales Prospects Tracker.md`) are local markdown — read them directly with the file tools.

## Workflow
1. **Resolve identifier & log source** — Confirm the identifier(s). Auto-detect the tracker from the selected folder per the table above.
2. **Tracker brief & deal fingerprint** — Read the matching tracker. Extract the row(s): stage/status, owner, value/opportunity, source (original lead #), last activity, next step. From the Deal paragraph, build the **deal fingerprint** (product, agent names, commercial keywords, reference codes) used to filter every other source. Note the tracker source. If no match, say so and list the closest name(s) for disambiguation.
3. **Emails (60 days)** — Delegate to **daily-emails `topic`** using each identifier as keyword. Classify each thread on-deal vs adjacent against the fingerprint. On-deal → main table: date (SGT), direction, parties, ≤40-word summary, action. Adjacent → hold for the Adjacent list.
   - **Thread genesis (don't silently drop origin context).** An on-deal thread often *starts before* the window but has recent in-window messages. Do not truncate it to only the in-window messages without flagging the rest. For any on-deal thread whose first message predates the window start, add a one-line **Thread genesis** note under the email table: `↳ Thread "<subject>" began <first-message date> (<N> messages before window; <M> in window)` and one phrase on what kicked it off (e.g. "9 Mar intro call → Aisha looped in for back-office"). This preserves how the deal originated even when the window excludes it. Rank threads by most-recent in-window message.
4. **Drive files & minutes (60 days)** — Delegate to **daily-files `topic`**. Keep only fingerprint-matching files (drop generic entity matches). Call out meeting minutes specifically and flag the most recent.
5. **Meetings (60 days)** — Delegate to **daily-calendars `search`**. Run one search **per identifier** (company, person, and email/domain) to find candidates, then **filter each event by the deal fingerprint** — an event that matches only the contact/domain but is off-topic (e.g. a relationship or portfolio meeting) goes to Adjacent, not the main table. List date (SGT), title, attendees, minutes link.
6. **Synthesize** — Executive summary: where the deal stands, momentum (warming/stalling), open actions with owners, recommended next step. Append the **Adjacent** list of entity-matched-but-off-deal touchpoints so nothing looks hidden.

## Output Skeleton (chat only)
```markdown
# Prospect Brief: {{Name / Company}}
*Generated: {{SGT timestamp}} · Window: last 60 days · Source tracker: {{Lead Gen Log | Sales Prospects Tracker | both}}*

## Snapshot
- **Stage / status:** {{from tracker}}
- **Owner:** {{Mary / Donny / other}}
- **Opportunity / value:** {{if any}}
- **Last activity:** {{date + what}}
- **Next step:** {{from tracker or recommended}}

## Executive Summary
- {{Where it stands + momentum + recommended next action}}
- {{Key risk or opportunity}}

## Emails (Last 60 Days)
| Date (SGT) | Dir | Parties | Summary | Action |
| --- | --- | --- | --- | --- |
| {{row}} |
_Fallback_: "No emails in last 60 days."
↳ _Thread genesis (only when an on-deal thread predates the window):_ Thread "{{subject}}" began {{date}} ({{N}} msgs before window; {{M}} in window) — {{what started it}}

## Meetings (Last 60 Days)
| Date (SGT) | Meeting | Attendees | Minutes |
| --- | --- | --- | --- |
| {{row}} |
_Fallback_: "No meetings in last 60 days."

## Drive Files & Minutes
{{Embed daily-files listing; flag most recent minutes}}
_Fallback_: "No files in last 60 days."

## Tracker Entry
> {{Verbatim / summarized row from Lead Gen Log or Sales Prospects Tracker, with source labeled}}

## Adjacent — Same Contacts, Different Context
*(entity-matched but not this deal — shown for visibility, not counted as momentum)*
- {{Date}} — {{item}} — _why off-deal_ {{e.g. loan repayment; portfolio/relationship meeting}}
_Omit this section only if there are genuinely no adjacent items._
```

## Guardrails
- All timestamps in **Singapore Time (SGT, UTC+8)**.
- Keep it tight — bullets and sentence fragments ≤40 words. This is a fast prep brief, not a report.
- Apply transcription corrections silently in any minutes/transcripts (Jack→Jeg, VCOM→WeCom, DSDA→DSTA).
- Every empty section states its fallback line rather than being omitted.
- One lead/prospect per invocation. If the identifier matches multiple, list candidates and ask which.

## Quality Gate
- Tracker source is always labeled (Lead Gen Log, Sales Prospects Tracker, or both).
- Every touchpoint is classified on-deal (main tables) or Adjacent — never mix relationship/off-topic items into deal momentum.
- Deal-topic relevance overrides the tracker log when they disagree (Adjacent + cross-reference note).
- ≤7 rows per table unless Christopher asks for more.
- On-deal threads that predate the window carry a **Thread genesis** note — origin context is never silently dropped.
- Meeting minutes explicitly identified where they exist.
- Drive searches are **title-scoped with content snippets excluded** by default (a `fullText` sweep overflows on active prospects); only fall back to `fullText` when a title search finds nothing.
- Native connectors only — no Zapier calls anywhere in the chain.
```
