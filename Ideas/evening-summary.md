# Evening Summary Skill Idea

## Opportunity
- No existing end-of-day workflow comparable to the structured morning brief.
- Lack of standardized capture for outcomes, pending items, and preparation for the next day.

## Proposed Solution
1. Create `evening-summary/skill.md` alongside existing skills to keep the catalog consistent.
2. Draft YAML header and overview mirroring other skills for uniform metadata.
3. Support manual "Evening Summary" command and optional scheduled nightly execution (timezone: Asia/Singapore).
4. Aggregate inputs from the following data sources:
   - **Calendar recap:** Completed events, attendance, key decisions, cancellations/reschedules.
   - **Email wrap-up:** Unread or unresolved threads, especially those with action items.
   - **Drive activity:** Files modified today needing review or archiving.
   - **Workday meeting minutes:** Notes stored in Workday folders, highlighting decisions, action items, and follow-ups.
   - **News snapshot:** Pull top 2–3 relevant headlines from trusted outlets (e.g., Google News API, RSS feeds) filtered for key topics (industry, major clients, macro trends).
   - **Task roll-over:** Outstanding items from the morning brief plus new obligations logged during the day.
   - **Tomorrow preview:** First events or deadlines for the next workday.
5. Produce an output structure with sections like "Today’s Highlights," "Outstanding Actions," "News & Market Watch," and "Tomorrow’s First Commitments" using concise executive bullets similar to the morning brief.
6. Document detailed tool usage (Gmail searches, Calendar queries, Drive scans, Workday folder access, news API queries) so future agents can reproduce the workflow.
7. Include error-handling guidance (e.g., note missing data if an integration fails or if news feeds are unavailable) and provide example invocation/output to set expectations.

## Example Evening Summary Output
- **Today’s Highlights**
  - Wrapped up "Q2 GTM Strategy" workshop; aligned on regional launch roadmap and assigned follow-up analysis to Sales Ops.
  - Resolved four high-priority email threads, including approval of the updated vendor contract and confirmation of the design review schedule.
  - Uploaded finalized meeting minutes for "APAC Partner Sync" to the Workday/Meetings/2024-06 folder with decisions and owners documented.
- **Outstanding Actions**
  - Prepare budget variance slides for tomorrow’s leadership stand-up; draft is in Drive: Finance/2024/Budgets.
  - Follow up with Legal on redlines for the vendor contract—waiting on revised clauses.
  - Review Workday task "Submit hiring justification" before 10:00 SGT tomorrow.
- **News & Market Watch**
  - TechCrunch: "Regional SaaS adoption surges 25% in APAC" – assess implications for Q3 pipeline; share key stats in tomorrow’s stand-up.
  - Straits Times: "Singapore introduces new data compliance guidelines" – coordinate with Legal to confirm any vendor impacts.
- **Tomorrow’s First Commitments**
  - 09:00–09:30 SGT: Leadership stand-up (Zoom) – bring finalized budget variance slides.
  - 10:30–11:00 SGT: Customer health check with Apex Corp – confirm implementation timeline.
  - 14:00–15:00 SGT: Product roadmap sync – ensure Workday meeting minutes template is ready for quick capture.

## Expected Impact
- Creates a comprehensive daily closure routine, improving awareness of accomplishments and pending work.
- Ensures critical action items and follow-ups from emails, meetings, and Workday notes are tracked.
- Facilitates better preparation for the next workday through proactive review of upcoming commitments.
