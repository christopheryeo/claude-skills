# Scheduled Tasks — Alex (Dev) / Claude Skills

**Last updated:** 2026-04-15
**Purpose:** This file documents scheduled tasks for the Claude Skills workspace under Alex (Dev).

---

## 1. task-execution

- **Description:** (Claude Skills) Task Execution
- **Schedule:** 3am SGT, weekdays only (`0 3 * * 1-5`)
- **Status:** ✅ Enabled
- **Task file:** `/Users/chrisyeo/Documents/Claude/Scheduled/task-execution/SKILL.md`

### Prompt

```
Executes one 'New' task from the daily plans file in the Claude Skills workspace.

Workflow:
1. Find the latest Plans/YYYY-MM-DD-plans.md file
2. Pick the first 🆕 task
3. Execute the task's Action field
4. Update the plans file (🆕 → ✅, mark priority group done if all complete)
5. Write/append audit entry to Plans/YYYY-MM-DD Audit.md
Constraints: one task per run; update both plans + audit together; leave as 🆕 if execution fails.
```
