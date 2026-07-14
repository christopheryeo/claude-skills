# Retrieval Workflows

Read this reference for the recent, starred, actioned, topic, and stakeholders sub-commands.

## Contents

- [Recent](#sub-command-recent)
- [Starred](#sub-command-starred)
- [Actioned](#sub-command-actioned)
- [Topic](#sub-command-topic)
- [Stakeholders](#sub-command-stakeholders)

## Sub-Command: RECENT

**Purpose:** List recent emails across Inbox, Sent, Drafts, and Starred.

**Default:** Last 48 hours. Accepts custom timeframes.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. Calculate timeframe → Gmail query format
2. Search 4 categories: `in:inbox`, `in:sent`, `in:drafts`, `is:starred` (each with time filter, max 10 results)
3. Apply newsletter exclusion if requested: `-category:promotions -from:newsletter -from:noreply -from:no-reply -subject:unsubscribe`
4. Apply selective thread reading per shared token rules
5. Deduplicate starred emails (mark with ⭐, don't list twice)
6. Sort all results by most recent first
7. Generate ≤30-word summaries
8. Build Gmail links from message IDs
9. Output using shared executive table format

---

## Sub-Command: STARRED

**Purpose:** Surface starred/priority emails with action notes and follow-up prompts.

**Default:** Last 48 hours. Accepts custom timeframes, keyword, sender, and label filters.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. Confirm timeframe and filters (default 48 hours, top 20)
2. Build query: `is:starred` + timeframe + user filters
3. Search Gmail, sort by most recent
4. Fetch thread details for each result (full context — starred items are priority)
5. Deduplicate: if multiple starred messages in one thread, choose latest instance
6. Generate ≤30-word summaries focused on why it was starred / key action
7. Derive follow-up items: deadlines, pending tasks, waiting-on notes
8. Output executive table with additional **Key Follow-ups** section

### Starred-Specific Output Header

```markdown
# ⭐ STARRED EMAILS DIGEST
**[Date, Timezone] | Last [timeframe]**

## Snapshot
- **Starred emails reviewed:** [count]
- **Most recent starred:** [Subject] from [Sender] ([Time ago])
```

---

## Sub-Command: ACTIONED

**Purpose:** Blend recently sent emails + starred emails into a single executive recap.

**Default windows:** Sent = last 48 hours, Starred = last 7 days. User can override either or both.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. Confirm timeframes (separate windows for sent and starred)
2. Search `in:sent` with sent window (max 10 results)
3. Search `is:starred` with starred window (max 10 results)
4. For sent: use search metadata only (no full thread reads)
5. For starred: read full thread only for unread/important items (max 5 threads)
6. Deduplicate: if sent message is also starred, present once as `Sent ⭐`
7. Generate ≤25-word summaries
8. Extract follow-ups from starred items only
9. Output executive table with dual-window context header

---

## Sub-Command: TOPIC

**Purpose:** Search Gmail threads by topic/keyword and present a prioritised digest.

**Requires:** Topic keyword(s) from user. Optional: timeframe, participant filters, exclusions.

**Default:** Last 48 hours. Accepts custom timeframes.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. Clarify topic, timeframe (default 48 hours), exclusions, participant filters
2. Build query: `"{topic}"` or `subject:"{topic}"` + filters
3. Search Gmail (default 50 results)
4. Expand each unique thread for participants, timestamps, message IDs
5. Deduplicate and score: prioritise subject matches and recent messages
6. Flag decision points (approvals, blockers, action items)
7. Produce topic overview with top correspondents and coverage period

### Topic-Specific Output Format

```markdown
# 📂 TOPIC EMAIL DIGEST — {Topic}
**Query:** `{Gmail query}` | **Timeframe:** {Window} | **Threads reviewed:** {count}

## Snapshot
- **Top correspondents:** [names]
- **Total messages:** [count]
- **Coverage period:** [Oldest] → [Newest]

## Spotlight Threads
1. **[Subject]** — [Sender → Recipients] ([Date])
   *Why it matters:* [≤40-word summary]
   **Link:** [📧 Open Thread]

## Full Topic Log
(executive table format)

## Suggested Next Steps
- [Action items derived from emails]
```

---

## Sub-Command: STAKEHOLDERS

**Purpose:** Scan Gmail for emails from tracked stakeholder contacts and present a grouped digest.

**Requires:** A Monitor Stakeholders Command section in the applicable workspace instructions (`CLAUDE.md`, `AGENTS.md`, or equivalent) with inline stakeholder groups and email addresses.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. Read the Monitor Stakeholders Command section in the current workspace instructions — extract groups, contacts (Name, Role, Email), and monitoring notes
2. If no stakeholder list is found, ask the user: "No stakeholder list was found in the workspace instructions. Would you like to add one, or shall I show your recent emails instead?" If the user chooses recent, execute the **recent** sub-command instead
3. Default timeframe: last 48 hours (accepts custom)
4. For each stakeholder group, build query: `newer_than:2d (from:email1 OR from:email2 OR to:email1 OR to:email2)`
5. Run all group queries (parallel where possible)
6. Deduplicate by message ID across groups — assign to first matching group by sender
7. Fetch full thread for each unique message
8. Generate ≤30-word summaries

### Stakeholder-Specific Output

1. **Header** with date, timeframe, groups monitored count
2. **Executive table** with stakeholder group identifier in From/To column
3. **Groups with no activity** — list silent stakeholder groups
4. **Action Required** — flag emails matching monitoring notes (e.g., "board meeting scheduling", "ACRA filing"), plus unread/important/directly-addressed items
5. **Key Observations** — patterns and themes

---
