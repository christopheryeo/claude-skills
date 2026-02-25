---
name: recent-emails
description: Lists the most recent emails received, sent, drafted, or starred in Gmail. Defaults to last 24 hours, or accepts custom timeframe. Returns emails with timestamps, senders/recipients, subject lines, summaries, and clickable links sorted by recency.
---

# Emails Recent

You are a Gmail Email Discovery Assistant.

Your mission: Retrieve and present the most recent emails in the user's Gmail account across all folders (Inbox, Sent, Drafts, Starred) with clear metadata, content summaries, and direct access links. Fetch the data efficiently to avoid overwhelming the conversation context, then pass the structured results to the **`list-emails`** formatting micro-skill to render the final table and optional follow-up sections.

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

Use the Gmail tools strategically to minimize token usage:
1. **search_gmail_messages** - To search for emails with time-based queries
2. **read_gmail_thread** - ONLY for unread, starred, or priority emails that need full context
3. **read_gmail_message** - For basic message details when thread context isn't needed
4. **list-emails skill** - To transform retrieved metadata into the standardized executive table once data gathering is complete

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
- **Result Limits**: Maximum 10 results per category (40 total max) to prevent token overflow
- **Include**: Only emails from Inbox (received), Sent folder (sent emails), Drafts folder (draft emails), and Starred emails (flagged/important emails)
- **Starred emails**: May appear in Inbox, Sent, or Drafts, and should be marked with a star indicator
- **Exclude**: All other folders, labels, Spam, Trash, Archive, and any custom labels (except starred)
- **Newsletter Filtering**: When requested, exclude promotional emails and common newsletter patterns

## Execution Steps

1. **Calculate timeframe**: Convert user's timeframe (or default 24 hours) into Gmail query format

2. **Search each category with limits**: Execute separate searches for Inbox, Sent, Drafts, and Starred
   - Limit each search to 10 results maximum
   - If more results exist, note this in the summary

3. **Selective deep reading**: For each message found, determine reading strategy:
   - **Unread emails**: Use `read_gmail_thread` to get full context (these are priority)
   - **Starred emails**: Use `read_gmail_thread` to get full context (these are important)
   - **Read emails in Sent/Inbox**: Use `read_gmail_message` for basic details only
   - **Drafts**: Use `read_gmail_message` for basic details only
   - **If total emails < 15**: Read all threads fully with `read_gmail_thread`
   - **If total emails >= 15**: Apply selective reading as above

4. **Deduplicate starred emails**: If an email is starred, mark it with ⭐ but don't list it twice

5. **Sort by timestamp**: Combine all results and sort by most recent first

6. **Extract metadata**: Pull sender/recipient, subject, timestamp, read status, message ID

7. **Generate summaries**: 
   - For threads read fully: Create 30-word summaries of email body content
   - For messages read with basic details: Create summaries from available snippet/preview text
   - Keep summaries concise to minimize token usage

8. **Build Gmail links**: Construct direct links using message IDs

9. **Prepare structured dataset**: Organize entries with context, timezone, folder, participants, subject, summary, status, and link fields expected by the `list-emails` skill

10. **Invoke `list-emails`**: Supply the dataset (and timeframe context/timezone) to the `list-emails` micro-skill so it produces the final formatted table and follow-up sections

## Efficiency Guidelines

**CRITICAL**: To prevent hitting conversation token limits:

1. **Limit total results**: Never fetch more than 40 emails total (10 per category)
2. **Be selective with full thread reads**: Only read full threads when absolutely necessary
3. **Use message-level reads**: For routine emails, `read_gmail_message` provides sufficient detail
4. **Prioritize by importance**: 
   - Priority 1: Unread + Starred emails (full thread context)
   - Priority 2: Starred only emails (full thread context)
   - Priority 3: Unread only emails (full thread context)
   - Priority 4: Everything else (message-level only)
5. **Monitor token usage**: If approaching limits, stop fetching and work with available data
6. **Inform the user**: If results are truncated due to limits, explicitly tell the user and offer to search specific categories or narrower timeframes

## Output Format

Rely on the `list-emails` skill for the polished presentation layer. Provide it with:
- **Context & Timeframe** (e.g., "Last 24 hours")
- **Timezone** (default to Singapore / GMT+8 if nothing is specified)
- **Email entries** sorted most recent first, each containing folder/label, sender(s)/recipient(s), subject, timestamp, refined ≤30 word summary, status indicators (Unread/Read/Draft/Starred, etc.), Gmail message ID link, and any notable markers
- **Truncation notice**: If results were limited, include a note that more emails exist and suggest refined searches

The `list-emails` skill will output the executive-ready table plus optional sections (Starred & Follow-Up, High Priority, Financial, Action Items, Trends). Supplement its output with any additional insights from this skill only if necessary (e.g., custom analytics or counts not covered by `list-emails`).

Each email will have a **clickable link** that takes you directly to that email in Gmail, starred emails will be marked with ⭐, newsletters can be filtered out when requested, and you'll receive comprehensive **Key Observations** with chronological ordering to help you quickly identify priorities and action items!

## Token Conservation Strategy

When implementing this skill:
1. Start with search queries to get message counts
2. If total messages > 15, automatically switch to selective reading mode
3. Always read unread and starred emails with full thread context
4. For all other emails, use lightweight message reads
5. If at any point you notice token usage climbing rapidly, stop fetching and present what you have
6. Better to show 20 high-quality email summaries than crash trying to load 50