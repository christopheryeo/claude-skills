---
name: customer-brief
description: Generate an executive-ready customer brief that fuses internal touchpoints, deliverables, and external market intelligence into a single actionable digest before key account interactions.
---

# Customer Brief

Create a consolidated, audit-friendly briefing on an individual customer that blends recent internal activity with curated external insights so relationship teams can walk into every touchpoint fully prepared.

## Overview

This skill orchestrates a multi-source review to surface:
- A crisp executive summary of customer health, momentum, and immediate asks
- The latest communications, meetings, and deliverables tied to the account
- Emerging risks, opportunities, and market signals worth raising with stakeholders
- Documented search keywords, timestamps, and source URLs for compliance-ready traceability

The voice should remain confident, empathetic, and professional—mirroring the Sentient.io brand guidance on clarity and credibility.

## Intended Users

- Account directors preparing pre-call briefs
- Customer success managers tracking follow-ups and risks
- Executive sponsors needing fast situational awareness

## Triggers

Invoke when a user says:
- "Run a customer brief for [Account]"
- "Prepare the [Account] touchpoint digest"
- "What do I need to know before meeting [Account]?"

## Success Criteria

Deliverables are considered complete when the brief:
- Captures top 3–5 highlights with sentiment indicators and next actions
- Lists up to seven recent communications with channel, parties, summary, sentiment, and actions
- Surfaces the next seven calendar events with normalized date/time and preparation notes
- Flags overdue deliverables, blockers, or open approvals explicitly
- Includes at least three external insights (or states "No new items in last 14 days" when applicable) with citation URLs
- Logs search keywords, date ranges, and data sources consulted for auditing

## Guardrails & Assumptions

**Does:**
- Aggregate internal context from email, calendar, shared files, and task trackers
- Curate public web intelligence (corporate site, newsrooms, press, blogs, analyst coverage)
- Distinguish clearly between internal and external data with labeled sections
- Annotate items requiring follow-up with owners and due dates

**Does Not:**
- Connect directly to CRM platforms or proprietary customer databases
- Summarize confidential chat transcripts without explicit user-provided exports
- Scrape gated or credential-protected content

**Limitations:**
- External research defaults to the past 14 days; state when extending the window
- Social media scanning limited to publicly accessible posts
- Sentiment analysis provides confidence scores but is not a substitute for human review

**Assumes:**
- Email and calendar integrations are authorized and scoped to the account workspace
- Shared file repositories expose metadata (owner, last modified, status)
- Users can provide supplemental context when automated retrieval fails

## Pre-Execution Checklist

1. Confirm the account name or unique identifier and primary timezone
2. Verify access to:
   - Email labels/folders tagged to the customer
   - Calendar events including agenda notes and attendees
   - Shared drive or collaboration workspace for deliverables
   - Internal task tracker exports or spreadsheets (if applicable)
3. Document the web search plan:
   - Keywords and Boolean variations (e.g., "<Account> press release", "<Account> partnership")
   - Date filter (default last 14 days)
   - Target sources (corporate site, trusted news outlets, industry reports)
4. Initialize sentiment scoring rubric (Positive / Neutral / Negative + confidence %)
5. Open an audit log to capture timestamps, connectors used, and notable exceptions

## Workflow

### 1. Gather Internal Communications
- Use email search to pull latest starred, recent, or action-required threads tagged with the customer
- Extract: received/sent date (local timezone), participants, concise summary (≤40 words), sentiment, required action, owner
- If no emails found in past 14 days, state "No recent communications" and point to archive or CRM alternatives

### 2. Compile Upcoming Touchpoints
- Query calendar for next meetings including the account team or customer stakeholders
- Normalize times to the primary account timezone while noting any multi-timezone adjustments
- Capture meeting title, date, time, organizer, participants, prep tasks, and attachments/reference docs
- Highlight meetings flagged as critical (e.g., QBR, renewal negotiation)

### 3. Review Deliverables & Files
- List latest documents from shared drives or collaboration spaces tied to the account
- Include file name, owner, status (Draft/In Review/Approved/Overdue), last modified date, and link/path
- Flag overdue deliverables in bold with recommended follow-up actions

### 4. Aggregate Task Tracker Items
- Import rows from spreadsheets or lightweight trackers
- Present open items with owner, due date, status, and blocker notes
- Note gaps if tracker data is unavailable or stale

### 5. Conduct External Research
- Execute web searches using documented keywords and filters
- Capture top relevant URLs (max 5) with source name, headline, publish date, and 1–2 sentence impact summary
- Differentiate categories: corporate updates, press/newsroom, analyst/industry coverage, competitive signals
- Record search log: keywords, filters, timestamp, results count, and discarded sources (if notable)

### 6. Assess Risks & Opportunities
- Synthesize recurring themes from communications, tasks, and external intel
- Classify items under **Risks**, **Opportunities**, and **Watchlist** with recommended owner and next step
- Highlight sentiment shifts or at-risk deliverables triggering escalation thresholds (e.g., two consecutive negative emails)

### 7. Assemble Executive Summary
- Draft 3–5 bullets covering health, key blockers, immediate next actions, and strategic signals
- Reference supporting sections inline (e.g., "See Deliverables #2")
- Maintain confident yet empathetic tone per Sentient.io guidelines

### 8. Produce Audit Trail
- Append a log detailing:
  - Data sources queried, connectors used, and timestamps
  - Search keywords and filters applied
  - Manual inputs or overrides supplied by user
- Store audit log metadata for reuse in follow-up briefs

## Output Template

```markdown
---
# Customer Brief: {{Account Name}}
*Generated: {{Local Timestamp}} | Primary Timezone: {{TZ}}*

## Executive Summary
- [Bullet 1: sentiment + actionable insight]
- [Bullet 2]
- [Bullet 3]

## Recent Communications (Last 14 Days)
| Date ({{TZ}}) | Channel | Parties | Summary | Sentiment | Action Required |
| --- | --- | --- | --- | --- | --- |
| 2025-03-18 09:30 | Email | A. Director ↔ Customer PM | Scope alignment follow-up | Neutral (65%) | Confirm revised timeline |

_Fallback_: "No new communications in last 14 days. Review archive label: {{Label}}."

## Upcoming Touchpoints
| Date | Time ({{TZ}}) | Meeting | Owner | Prep Notes |
| --- | --- | --- | --- | --- |
| 2025-03-21 | 14:00 | Q1 Renewal Readiness | J. Lee | Review deck v3, confirm pricing guardrails |

## Deliverables & Files
- **Proposal v4** — Owner: R. Singh — Status: In Review — Updated: 2025-03-17 — [Drive Link]
- **Security Questionnaire** — Owner: M. Chen — Status: Overdue (due 2025-03-15) — Escalate to Infosec

## Risks & Opportunities
- **Risk:** Timeline slip on security review; request expedited legal review (Owner: M. Chen)
- **Opportunity:** Customer exploring APAC expansion; prepare analytics upsell (Owner: BD Team)

## Competitive / Market Watch
1. _Reuters_ (2025-03-16) — {{Headline}} — {{Impact statement}} — [URL]
2. _Industry Blog_ (2025-03-15) — {{Headline}} — {{Impact statement}} — [URL]

## External Web Highlights
- {{Source}} — {{Headline}} — {{1–2 sentence summary with actionable takeaway}} (URL)

## Search Log & Audit Notes
- Keywords: "{{Account}} press release", "{{Account}} partnership"
- Date Filter: Last 14 days (2025-03-04 → 2025-03-18)
- Sources Queried: Corporate site, newsroom, Reuters, LinkedIn
- Exceptions: Unable to access internal tracker; requested manual update from owner
```

## Quality Checklist

Before delivering the brief, verify:
- [ ] All tables contain ≤7 entries unless user explicitly requests full export
- [ ] Sentiment labels include confidence percentages
- [ ] Internal vs external sources are clearly labeled
- [ ] Every external insight references a valid, accessible URL
- [ ] Overdue items or negative sentiment threads are highlighted with follow-up owners
- [ ] Audit log details search parameters and connectors used

## Testing & Validation Notes

- Dry run with mock data covering: (a) active account with rich activity, (b) dormant account with minimal signals, (c) conflicting sentiment inputs
- Validate timezone normalization by comparing calendar entries across at least two regions
- Stress test with dense email threads to ensure summaries stay under 40 words
- Confirm fallback messaging renders when a section has no data

## Deployment & Packaging

- Store this file at `customer-brief/skill.md` with YAML front matter
- Include invocation phrases, workflow notes, and testing instructions above when packaging the skill manifest
- When ready for release, zip the `customer-brief` directory and follow repository deployment workflow for upload and catalog registration

## Future Enhancements

- Define quantitative thresholds for "at-risk" status (e.g., ≥2 overdue deliverables or consecutive negative sentiment entries)
- Evaluate compliance considerations for proactive social monitoring with legal/PR partners
- Integrate optional CRM exports if approved in future roadmap
