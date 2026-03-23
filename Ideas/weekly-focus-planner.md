# Weekly Focus Planner Skill Idea

## Opportunity
- Existing productivity skills cover daily rituals (morning orchestration, evening summary) but lack a structured weekly planning cadence.
- Users need a consolidated snapshot of the coming week’s meetings, deliverables, and external signals to align priorities proactively.
- Reuses current integrations (Gmail, Calendar, Drive, news) to minimize implementation overhead while increasing strategic value.

## Proposed Solution
1. Add `weekly-focus-planner/skill.md` to the catalog with metadata aligned to other skills.
2. Support manual triggers such as “Plan my week” and scheduled Monday morning delivery, with configurable planning horizons (default: next 7 days).
3. Aggregate and synthesize data from:
   - **Calendar horizon scan:** Flag high-impact meetings, travel, and deadlines; group by theme or strategic pillar.
   - **Email follow-ups:** Surface unresolved or promised items that require action during the upcoming week.
   - **Drive artifacts:** Highlight documents needing review or completion before key meetings.
   - **Project/task roll-ups:** Capture outstanding actions from Work Day folders or tracked spreadsheets.
   - **News & external signals:** Include 2–3 relevant headlines to inform positioning for the week.
4. Structure output as:
   - **Executive Snapshot:** Three bullets summarizing overarching goals, risks, and context.
   - **Priority Meetings & Prep:** Table with date/time, participants, objective, and prep assets.
   - **Deliverables Due:** Checklist of documents or outputs to finalize, with owners and source links.
   - **Follow-up Queue:** Outstanding emails/tasks with target resolution dates before week’s end.
   - **Watchlist:** External developments (news, policy changes, competitor moves) influencing priorities.
   - **Focus Guardrails:** Suggested focus blocks, no-meeting windows, and delegation opportunities.
5. Implement guardrails to:
   - Default to rolling 7-day windows starting next business day; allow custom ranges.
   - Limit each section to the top 5–7 items, referencing where to find full lists.
   - Label confidence levels when data sources are incomplete and log retrieval timestamps.
   - Encourage user confirmation or adjustment of priorities to maintain a co-pilot dynamic.

## Example Weekly Focus Output
- **Executive Snapshot**
  - Solidify Q3 launch readiness while protecting dedicated time for strategic planning.
  - Manage partner alignment sessions and finalize the regional budget narrative.
  - Monitor industry regulatory changes that could shift compliance requirements.
- **Priority Meetings & Prep**
  - Tue 10:00–11:00: Q3 launch checkpoint (Marketing, Product) – review Drive: Launch/Q3/readiness-deck.
  - Wed 14:00–15:00: Partner ecosystem sync (Alliances) – prep meeting brief in Work Day/Partners/2024.
  - Fri 09:00–09:45: Finance review (CFO, Ops) – update budget narrative in Drive: Finance/2024/Q3.
- **Deliverables Due**
  - Finalize Q3 budget narrative – owner: Ops; due Thu 17:00.
  - Send follow-up summary to Apex Corp after Tuesday’s sync – owner: Account Lead; due Wed 12:00.
- **Follow-up Queue**
  - Respond to Legal’s contract redlines (email thread “Vendor MSA rev2”) before Tue EOD.
  - Confirm executive briefing agenda with CEO office (calendar hold Fri 16:00).
- **Watchlist**
  - Industry headline: “APAC data privacy standards tightening in 2024” – coordinate with Legal for readiness.
  - Competitor: “Nimbus launches AI onboarding assistant” – review implications for customer messaging.
- **Focus Guardrails**
  - Block Wed 09:00–11:00 for deep work on launch readiness plan.
  - Delegate weekly metrics update to Analytics team; schedule review Thu 13:00.

## Expected Impact
- Bridges daily execution with strategic weekly planning, enabling proactive prioritization.
- Provides repeatable Monday ritual, reducing cognitive load and context switching.
- Strengthens adoption of existing integrations by weaving them into a higher-level workflow.
