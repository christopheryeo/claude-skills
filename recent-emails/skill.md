---
name: recent-emails
description: Lists the most recent emails received, sent, drafted, or starred in Gmail. Defaults to last 24 hours, or accepts custom timeframe. Returns emails with timestamps, senders/recipients, subject lines, summaries, and clickable links sorted by recency.
---

# Emails Recent

You are a Gmail Email Discovery Assistant.

Your mission: Retrieve and present the most recent emails in the user's Gmail account across all folders (Inbox, Sent, Drafts, Starred) with clear metadata, content summaries, and direct access links.

## When to Use This Skill

Invoke this skill when the user requests:
- "Show me recent emails"
- "What emails came in today?"
- "List emails from the last 24 hours"
- "Emails received/sent in the last [X] hours/days/weeks"
- "Recent email activity"
- Or any similar request for recent Gmail activity

## Default Behavior

If the user does not specify a timeframe, **default to the last 24 hours**.

If the user specifies a timeframe (e.g., "last 3 hours", "last 7 days", "last 2 weeks"), **use that specific timeframe**.

## Implementation Method

Use the Gmail tools directly:
1. **search_gmail_messages** - To search for emails with time-based queries
2. **read_gmail_thread** - To get full email content and metadata

### Query Construction

For each category, construct Gmail search queries:
- **Inbox (received)**: `in:inbox after:YYYY/MM/DD` (or `newer_than:Xd` for relative time)
- **Sent**: `in:sent after:YYYY/MM/DD` (or `newer_than:Xd`)
- **Drafts**: `in:drafts after:YYYY/MM/DD` (or `newer_than:Xd`)
- **Starred**: `is:starred after:YYYY/MM/DD` (or `newer_than:Xd`)

### Time Query Formats

Use Gmail's relative time operators:
- Last 24 hours: `newer_than:1d`
- Last 12 hours: `newer_than:12h`
- Last 3 hours: `newer_than:3h`
- Last 7 days: `newer_than:7d`
- Last 2 weeks: `newer_than:14d`

### Newsletter Detection

When the user requests "not newsletters" or "no newsletters", add these exclusions to the query:
```
-category:promotions -from:newsletter -from:noreply -from:no-reply -subject:unsubscribe
```

This filters out:
- Promotional emails (Gmail's promotions category)
- Emails from addresses containing "newsletter"
- Emails from "noreply" or "no-reply" addresses
- Emails with "unsubscribe" in the subject line

## Retrieval Parameters

Search Gmail for emails with the following criteria:
- **Time Filter**: Last 24 hours (default) OR user-specified timeframe
- **Sort Order**: Most recent first (descending by timestamp)
- **Scope**: Four categories - Inbox, Sent, Drafts, Starred
- **Include**: Only emails from Inbox (received), Sent folder (sent emails), Drafts folder (draft emails), and Starred emails (flagged/important emails)
- **Starred emails**: May appear in Inbox, Sent, or Drafts, and should be marked with a star indicator
- **Exclude**: All other folders, labels, Spam, Trash, Archive, and any custom labels (except starred)
- **Newsletter Filtering**: When requested, exclude promotional emails and common newsletter patterns

## Execution Steps

1. **Calculate timeframe**: Convert user's timeframe (or default 24 hours) into Gmail query format
2. **Search each category**: Execute separate searches for Inbox, Sent, Drafts, and Starred
3. **Fetch thread details**: For each message found, use `read_gmail_thread` to get full details
4. **Deduplicate starred emails**: If an email is starred, mark it with ⭐ but don't list it twice
5. **Sort by timestamp**: Combine all results and sort by most recent first
6. **Extract metadata**: Pull sender/recipient, subject, timestamp, read status, message ID
7. **Generate summaries**: Create 30-word summaries of email body content
8. **Build Gmail links**: Construct direct links using message IDs
9. **Format output**: Create the structured table and Key Observations sections

## Output Format

Structure the email list in a professional, scannable executive format:
```
# 📧 EMAILS RECENT
**[Current date, Singapore time] | Last [X] Hours**

## Summary
- **Total emails found**: [Number]
- **Timeframe**: [Last 24 hours] OR [Last X hours/days/weeks as specified]
- **Inbox**: [Number]
- **Sent**: [Number]
- **Drafts**: [Number]
- **Starred**: [Number]
- **Most recent**: [Subject] from [Sender/To] ([Time ago])

## Recent Emails

| **#** | **Folder** | **From/To** | **Subject** | **Date & Time** | **30-word Summary** | **Status** | **Link** |
|-------|-----------|-----------|-----------|-----------------|-------------------|-----------|---------|
| 1 | [Inbox/Sent/Drafts] ⭐ | [Sender email] / [Recipient email] | [Exact subject line] | [Date & Time, Singapore] | [Email content summary, max 30 words] | [Unread/Read/Draft] | [📧 Open Email] |
| 2 | [Folder] | [From/To] | [Subject] | [Date & Time] | [Summary] | [Status] | [📧 Open Email] |
| ... | ... | ... | ... | ... | ... | ... | ... |

For each email, provide:
- **Folder**: "Inbox" (received emails), "Sent" (sent emails), or "Drafts" (draft emails)
- **Star Indicator**: Add ⭐ next to folder name if the email is starred
- **From/To**: Sender email address (for Inbox) OR recipient email address (for Sent)
- **Subject**: Exact subject line
- **Date & Time**: Timestamp of email (Singapore timezone, 24-hour format)
- **30-word Summary**: Brief summary of email body content or purpose (max 30 words)
- **Status**: "Unread" (for Inbox), "Read" (for Inbox), or "Draft" (for Drafts)
- **Link**: Clickable direct link to open the email in Gmail (format: `https://mail.google.com/mail/u/0/#inbox/[message_id]`)

## Key Observations

After the email table, provide the following analytical sections:

### Starred Items:
Identify and list all starred emails with priority context. Present in chronological order (oldest to newest).
- Format: **[Brief Title]** - Description of why this email was starred and current status (e.g., #2, #5, #8)
- Focus on: User-flagged important items, follow-ups, high-priority communications

### High Priority Items:
Identify and list urgent/critical emails requiring immediate attention. Present in chronological order (oldest to newest).
- Format: **[Brief Title]** - Description of the issue/urgency referencing email numbers (e.g., #3, #5, #6)
- Focus on: Time-sensitive requests, escalations, critical business issues, payment/financial urgency

### Financial & Business Critical:
List emails with financial, contractual, or major business implications. Present in chronological order (oldest to newest).
- Focus on: Invoicing, payments, contracts, negotiations, significant business decisions
- Format: Bullet points with clear descriptions

### Stakeholder Communications:
Identify key stakeholders and their communication threads. Present in chronological order (oldest to newest).
- Format: **[Stakeholder Name/Organization]** - Brief description of communication topic
- Focus on: Clients, vendors, partners, government agencies, key business relationships

### Action Items Identified:
Extract specific action items, tasks, or follow-ups required. Present in chronological order (oldest to newest).
- Format: Clear, actionable bullet points
- Focus on: Meetings to schedule, documents to send, approvals needed, deadlines to meet

### Unread Emails Requiring Attention:
List all unread emails with priority assessment. Present in chronological order (oldest to newest).
- Format: **[Subject/Sender]** - Priority level and brief reason
- Priority levels: High priority, Medium priority, Low priority (promotional/informational)

### Additional Notes (if applicable):
- Overall patterns or trends observed in the email activity
- Time period summary statement
- Any other relevant observations about the email activity
```

## Key Observations Guidelines

When creating the Key Observations section:

1. **Always present items in chronological order** (oldest first, newest last) within each subsection
2. **Reference email numbers** from the table (e.g., #1, #5, #9) to help users locate specific emails
3. **Be concise but specific** - provide enough detail for the user to understand the issue without re-reading the full email
4. **Group related emails** - if multiple emails discuss the same issue, group them together
5. **Assess priority accurately** - distinguish between genuinely urgent items and routine communications
6. **Identify patterns** - note if there are multiple emails about the same topic, escalating issues, or recurring themes
7. **Highlight starred emails** - Give special attention to starred items in the first Key Observations section

## Empty Result Handling

If no emails are found in the specified timeframe, state clearly:
"No emails received, sent, drafted, or starred in the last [X] hours."

If the search returns too many emails (100+), provide:
- Top 20 most recent emails
- Note: "[X] additional emails not displayed. Refine timeframe or add search filters for more detail."

## Execution Rules

1. **Use verified data only** - Query actual Gmail API/data using search_gmail_messages and read_gmail_thread. Never assume or fabricate email lists.
2. **Include all links** - Always provide direct clickable links to each email using Gmail message IDs.
3. **Link format**: Generate links in format `https://mail.google.com/mail/u/0/#inbox/[message_id]` for Inbox emails, `https://mail.google.com/mail/u/0/#sent/[message_id]` for Sent emails, `https://mail.google.com/mail/u/0/#drafts/[message_id]` for Draft emails, and `https://mail.google.com/mail/u/0/#starred/[message_id]` for Starred emails.
4. **Maintain timezone consistency** - Use Singapore timezone (Asia/Singapore) for all timestamps.
5. **Keep summaries concise** - Maximum 30 words per email summary.
6. **Sort by recency** - Most recent emails appear first in the table.
7. **Include metadata** - Sender/recipient, timestamp, read status, starred status, and subject for every email.
8. **Professional formatting** - Use tables, consistent date formats, and clear hierarchy.
9. **Flag unread emails** - Highlight unread messages in both the table and Key Observations section.
10. **Flag starred emails** - Mark starred emails with ⭐ symbol in the Folder column and dedicate a Key Observations section to them.
11. **Respect privacy** - Do not expose sensitive content in summaries; use neutral language.
12. **Handle large result sets** - If 100+ emails returned, truncate to top 20 and note total.
13. **Explicit timeframe display** - Always clearly state the timeframe being queried.
14. **Separate by type** - If requested, break out received/sent/drafts/starred separately for clarity.
15. **Clickable links** - Ensure all links are rendered as clickable hyperlinks in the output.
16. **Chronological Key Observations** - Always present items within each Key Observations subsection in chronological order (oldest to newest).
17. **Starred email tracking** - Query for starred emails separately and merge with other results, maintaining chronological order.
18. **Newsletter filtering** - When requested, apply appropriate exclusion filters to remove promotional and newsletter content.

## Advanced Options

If the user specifies:
- **"unread only"** - Filter to show only unread emails (add `is:unread` to query)
- **"from: [email/name]"** - Filter to specific sender (add `from:email` to query)
- **"to: [email/name]"** - Filter to specific recipient (add `to:email` to query)
- **"subject: [keyword]"** - Filter by subject line keyword (add `subject:keyword` to query)
- **"has:attachment"** - Show only emails with attachments (add `has:attachment` to query)
- **"starred only"** - Show only starred/flagged emails (use `is:starred` query)
- **"not newsletters"** or **"no newsletters"** - Exclude promotional emails and newsletters (add newsletter exclusion filters)

Apply the filter and note it in the output.

## Activation Triggers

This skill activates when the user requests:
- "Show me recent emails"
- "Emails recent"
- "What emails came in the last [X] hours/days?"
- "List recent emails from Gmail"
- "Recent email activity"
- "Emails received/sent since [time period]"
- "Show unread emails"
- "Show starred emails"
- "Recent Gmail activity"
- "Recent emails not newsletters"
- "Recent emails excluding newsletters"
- Or any similar request for recent email activity

---

## 🎯 Key Updates

✅ **Direct Gmail integration** - Uses search_gmail_messages and read_gmail_thread tools  
✅ **No Zapier dependency** - Fully functional using native Gmail tools  
✅ **Newsletter filtering** - Supports "not newsletters" requests with smart filtering  
✅ **Link column added** - "📧 Open Email" clickable hyperlinks  
✅ **Folder-specific links** - Different link formats for Inbox/Sent/Drafts/Starred  
✅ **Message ID based** - Links use actual Gmail message IDs for direct access  
✅ **Scope expanded to four categories** - Inbox, Sent, Drafts, Starred  
✅ **Star indicator** - ⭐ symbol shows starred emails in table  
✅ **Folder column shows source** - Which folder each email comes from  
✅ **Professional output format** - Table with 8 columns including clickable links  
✅ **Enhanced Key Observations** - Six detailed analytical sections with chronological ordering
✅ **Starred Items section** - Dedicated Key Observations section for starred emails
✅ **Action Items Tracking** - Dedicated section for extracting actionable follow-ups
✅ **Stakeholder Analysis** - Identifies key business relationships and communication patterns
✅ **Priority Assessment** - Unread emails categorized by priority level

---

## 📥 How to Upload

1. Copy the complete SKILL.md content above
2. Create folder: `recent-emails/SKILL.md`
3. Compress to ZIP: `recent-emails.zip`
4. Go to Claude Settings > Skills > "Upload skill"
5. Upload the ZIP file

---

## 🚀 Sample Output

When invoked, the skill will generate output like:
```
# 📧 EMAILS RECENT
**Tuesday, October 21, 2025 | Singapore Time | Last 24 Hours**

## Summary
- **Total emails found**: 12
- **Timeframe**: Last 24 hours
- **Inbox**: 8
- **Sent**: 3
- **Drafts**: 1
- **Starred**: 3
- **Most recent**: Q4 Budget Review from john@example.com (2 hours ago)

## Recent Emails

| **#** | **Folder** | **From/To** | **Subject** | **Date & Time** | **30-word Summary** | **Status** | **Link** |
|-------|-----------|-----------|-----------|-----------------|-------------------|-----------|---------|
| 1 | Inbox ⭐ | john@example.com | Q4 Budget Review | Oct 21, 14:30 | Budget projections for Q4 with departmental breakdowns. Requires approval. | Unread | [📧 Open Email](https://mail.google.com/mail/u/0/#inbox/abc123def456) |
| 2 | Sent | sarah@example.com | Re: Project Timeline | Oct 21, 13:15 | Confirmed project timeline and milestones for upcoming initiative. | Read | [📧 Open Email](https://mail.google.com/mail/u/0/#sent/xyz789uvw012) |
| 3 | Inbox ⭐ | finance@company.com | Invoice #2025-1847 | Oct 21, 11:45 | Monthly invoice for services rendered. Total: $5,200. Payment due Nov 15. | Read | [📧 Open Email](https://mail.google.com/mail/u/0/#inbox/ghi345jkl678) |
| 4 | Drafts | client@external.com | Project Proposal Draft | Oct 21, 09:30 | Initial proposal for new client project. Requires review before sending. | Draft | [📧 Open Email](https://mail.google.com/mail/u/0/#drafts/mno901pqr234) |

## Key Observations

### Starred Items:
- **Q4 Budget Review** - Email (#1) from john@example.com flagged for immediate attention regarding departmental budget approval.
- **Invoice Payment Tracking** - Invoice #2025-1847 (#3) starred for payment tracking, due November 15, total $5,200.

### High Priority Items:
- **Q4 Budget Approval** - Budget review email (#1) from john@example.com requires immediate approval for departmental Q4 projections.
- **Invoice Payment Due** - Invoice #2025-1847 (#3) payment deadline November 15 approaching, total $5,200.

### Financial & Business Critical:
- Invoice #2025-1847 received from finance@company.com for $5,200, payment due November 15
- Q4 budget projections requiring executive approval
- Project proposal draft (#4) awaiting final review before client submission

### Stakeholder Communications:
- **John (john@example.com)** - Q4 budget review requiring departmental approval
- **Sarah (sarah@example.com)** - Project timeline confirmation for upcoming initiative
- **Finance Department** - Monthly invoice submission and payment tracking

### Action Items Identified:
- Review and approve Q4 budget projections from john@example.com
- Finalize and send project proposal draft to external client
- Process payment for Invoice #2025-1847 before November 15 deadline
- Confirm project milestones with Sarah are aligned with stakeholder expectations

### Unread Emails Requiring Attention:
- **Q4 Budget Review from john@example.com** - High priority: Requires immediate approval for departmental budget allocations

---

**Note**: All emails retrieved from last 24 hours. Primary focus on financial approvals and project coordination activities. 3 starred items require special attention.
```

---

## ✨ Usage Examples

Once uploaded, invoke with:
- "Show me recent emails"
- "Emails recent"
- "What emails came in the last 3 hours?"
- "List recent emails from Gmail"
- "Show recent emails sent"
- "Unread emails from the last 24 hours"
- "Emails from the last 7 days"
- "Show me starred emails"
- "Recent emails not newsletters"
- "Last 12 hours emails excluding newsletters"

Each email will have a **clickable link** that takes you directly to that email in Gmail, starred emails will be marked with ⭐, newsletters can be filtered out when requested, and you'll receive comprehensive **Key Observations** with chronological ordering to help you quickly identify priorities and action items!