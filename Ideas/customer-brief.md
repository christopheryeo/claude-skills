# Customer Brief Skill Idea

## Mission
Provide account teams with a consolidated, actionable summary of a specific customer's current state by unifying internal signals (communications, meetings, deliverables) with external intelligence gathered via web research (corporate site, blogs, press, market news).

## Why It Matters
- Keeps relationship managers aligned on recent interactions, open commitments, and sentiment shifts.
- Surfaces upcoming obligations and deadlines across calendar and shared workspaces.
- Adds timely market and competitive context sourced from the public web to inform outreach and risk assessments.

## Primary Triggers
- "Run a customer brief for [Account]"
- "Prepare the [Account] touchpoint digest"
- "What do I need to know before meeting [Account]?"

## Data Sources & Pulls
1. **Email**: Recent or starred threads tagged to the customer, extracting sender, subject, sentiment, and required actions.
2. **Calendar**: Upcoming meetings involving the account team and customer stakeholders, including agenda notes and prep tasks.
3. **Drive/Docs**: Latest shared files or deliverables associated with the account workspace.
4. **Internal Task Trackers or Spreadsheets**: Open action items, deal stages, blockers maintained outside formal CRM tools (no direct CRM integrations).
5. **News & External Web Search**:
   - Corporate website updates, newsroom posts, and blogs.
   - Press releases, financial filings, and analyst coverage.
   - Industry and competitor news mentioning the customer.
   - Social media highlights (LinkedIn posts, Twitter updates) when publicly accessible.
   - Document search methodology: record keywords used, filter dates (default last 14 days), and capture top relevant URLs.

## Output Structure
1. **Executive Summary**: 3-5 bullet highlights covering sentiment, key risks, and immediate next steps.
2. **Recent Communications**: Table with columns for Date (local to primary account timezone), Channel, Parties, Summary, Sentiment, and Action Required. Include fallbacks when no new emails.
3. **Upcoming Touchpoints**: Calendar-style table listing meeting title, date/time (timezone normalized), owner, and preparation notes.
4. **Deliverables & Files**: Bulleted list or table of latest documents with owner, status, and link/context. Flag overdue or pending approvals.
5. **Risks & Opportunities**: Bullets categorizing blockers, escalation needs, expansion opportunities, or cross-sell leads.
6. **Competitive / Market Watch**: Snapshot of recent industry coverage and competitor moves affecting the customer.
7. **External Web Highlights**: Bullets summarizing notable findings from web research with source citations (URL + headline).

## Execution Rules & Guardrails
- Validate all data sources before inclusion; mark items as "Unverified" if corroboration is pending.
- Apply consistent sentiment labeling (Positive / Neutral / Negative) with optional confidence scores.
- Default timezone to the account's primary operating region; note if multiple regions are involved.
- Limit each table to top 5-7 entries unless user requests a full export, with overflow message pointing to source systems.
- Clearly distinguish internal data from external web intelligence and provide URLs for traceability.
- Log search keywords, sources consulted, and timestamps for auditing.

## Deployment Notes
- Follow existing skill packaging (YAML front matter + narrative) when creating `customer-brief/skill.md`.
- Reference brand and tone guidelines from `sentient-brand-guideline` to maintain voice consistency.
- Document invocation phrases and testing steps, including mock data setup and verification of web scraping modules.
- Include instructions for zipping and uploading the skill per the repository's deployment workflow.

## Open Questions
- What thresholds define "at-risk" status for deliverables or sentiment shifts?
- Are there compliance considerations for monitoring customer social media channels?

