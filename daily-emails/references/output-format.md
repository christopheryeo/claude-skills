# Email Output Format

Read this reference whenever email results must be rendered for the user.

## Shared: Output Formatting (replaces list-emails)

All retrieval sub-commands produce output using this built-in formatter. Do NOT call the separate `list-emails` skill.

### Executive Table Format

```markdown
# 📧 EMAIL LIST
**Context:** [Timeframe/Context]
**Timezone:** [Timezone, default Singapore / GMT+8]

| # | Folder/Label | From → To | Subject | Date & Time | Summary (≤35 words) | Status | Link |
|---|--------------|-----------|---------|-------------|----------------------|--------|------|
| 1 | Inbox ⭐ | sender@example.com → Me | Subject line | DD MMM YYYY HH:MM SGT | Concise summary. | 📩❗ Unread, Important | [📧 Open](https://mail.google.com/mail/u/0/#inbox/MSG_ID) |
```

### Status Icons

| Status | Display | When to use |
|--------|---------|-------------|
| Unread | 📩 Unread | Not yet opened |
| Read | ✓ Read | Has been viewed |
| Draft | 📝 Draft | Unsent in drafts |
| Sent | ✉️ Sent | Outbound message |
| Replied | ↩️ Replied | User replied |
| Forwarded | ➡️ Forwarded | Forwarded to others |
| Starred | ⭐ Starred | Flagged/important |
| Important | ❗ Important | Gmail auto-flagged |

Combine when applicable: `⭐✓ Starred, Read` or `📩❗ Unread, Important`.

### Link Format

Always: `[📧 Open](https://mail.google.com/mail/u/0/#FOLDER/MESSAGE_ID)` using actual message IDs from Gmail API.

### Additional Sections (include only when data supports)

After the table, add relevant sections from:
- **Starred & Follow-Up Items** — bullet list with row references and next steps
- **High Priority / Time Sensitive** — urgent emails with deadlines
- **Financial / Contractual** — items with monetary or legal impact
- **Action Items** — tasks derived from emails
- **Notable Trends** — overarching patterns

### Quality Checklist

Before finalizing any output: sequential numbering ✅, summaries ≤35 words ✅, working Gmail links with real message IDs ✅, timezone stated ✅, optional sections only when populated ✅.

---
