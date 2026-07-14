# Scheduled Tasks — Alex (Dev) / Claude Skills

**Last updated:** 2026-04-23 (SGT) — task-execution: email report added (Step 6)
**Purpose:** This file documents scheduled tasks for the Claude Skills workspace under Alex (Dev).

---

## 1. task-execution

- **Description:** (Claude Skills) Task Execution
- **Schedule:** 3am SGT, weekdays only (`0 3 * * 1-5`)
- **Status:** ✅ Enabled
- **Task file:** `/Users/chrisyeo/Documents/Claude/Scheduled/task-execution/SKILL.md`

- **Report delivery:** Results sent via HTML email to chris@sentient.io — audit file in Plans/ still created as before.

### Prompt

```
Executes one 'New' task from the daily plans file in the Claude Skills workspace.

Workflow:
1. Find the latest Plans/YYYY-MM-DD-plans.md file
2. Pick the first 🆕 task
3. Execute the task's Action field
4. Update the plans file (🆕 → ✅, mark priority group done if all complete)
5. Write/append audit entry to Plans/YYYY-MM-DD Audit.md

6. **Send Task Execution Report via Email**
Send a summary report to Christopher immediately — no approval needed:
- **To:** chris@sentient.io
- **Subject:** [AI Team] Task Execution (Claude Skills) — YYYY-MM-DD HH:MMh SGT (use current SGT date and time)
- **Body:** Include: task name and description, execution outcome (completed / blocked / in-progress), what was done, any issues encountered, and remaining 🆕 New tasks count for today.
- **Format: HTML. Set body_type to "html".** Use clean, professional HTML formatting with inline CSS. Use styled `<table>` tags with styled headers (`#2c3e50` background, white text), bordered cells, alternating row colours, and `<h2>` section headers with a blue underline for all structured data.

Do NOT save the report as a markdown file (the audit file in Plans/ is separate and still created as before).

**⚠️ Email Operations:** Use the `daily-emails` skill for all Gmail operations. The skill enforces the correct connector policy (native first, Zapier fallback).

Constraints: one task per run; update both plans + audit together; leave as 🆕 if execution fails. All timestamps use Singapore Time (SGT, UTC+8).
```
