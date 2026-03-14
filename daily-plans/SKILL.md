---
name: daily-plans
description: >
  Manages a daily task planning system using Plans/ in whatever folder is currently selected — creating plans, adding new tasks, executing tasks one-by-one, logging completed work, checking status, deleting tasks, and carrying forward incomplete items. Works from any mounted folder. Seven operations: CREATE, NEW, EXECUTE (one task per invocation), LOG, STATUS, DELETE (with auto-renumbering), CARRY-FORWARD. Use whenever the user says "plan my day", "create a plan", "new task", "add a task", "add task [X]", "execute the plan", "next task", "log task", "log that", "plan status", "what's the plan", "where are we", "carry forward", "carry over", "delete task", "remove task", "drop task", or provides a numbered task list. Do NOT trigger for "set up my workday", "what did I do today?", meeting prep, email drafting, or calendar searches.
---

# Daily Plans

A unified daily task planning system with seven operations: **create**, **new**, **execute**, **log**, **status**, **delete**, and **carry-forward**. All operations work with markdown files in a `Plans/` folder resolved dynamically from the user's selected workspace.

---

## Locating the Plans/ Folder

This skill is **folder-agnostic** — it works from whatever folder the user has selected (mounted).

1. **Determine the mounted root.** The user's selected workspace is the mount point (e.g., `/sessions/.../mnt/Sentient`, `/sessions/.../mnt/Mary (Marketing)`, etc.).
2. **Look for `Plans/` at that root.** Check if a `Plans/` directory already exists at the top level of the mounted folder.
3. **Create it if missing.** If no `Plans/` folder exists, create one at the mounted root.

All file operations use this resolved path. Never hardcode a specific parent folder.

## Detecting the Sub-Command

| Trigger phrases | Operation |
|---|---|
| "plan my day", "create a plan", provides a list of tasks | **create** |
| "new task", "add a task", "add task [X]" | **new** |
| "execute the plan", "run today's tasks", "start the plan", "next task" | **execute** |
| "log task", "log that", "log the task" | **log** |
| "plan status", "what's the plan?", "show plan", "where are we?" | **status** |
| "delete task [X]", "remove task [X]", "drop task [X]" | **delete** |
| "carry forward", "carry over", "pull yesterday's tasks" | **carry-forward** |

If the intent is ambiguous, ask which operation is intended — but usually context makes it obvious.

## File Locations and Naming

- **Plans file:** `<plans-path>/YYYY-MM-DD-plans.md`
- **Audit file:** `<plans-path>/YYYY-MM-DD Audit.md`

Use today's date unless the user specifies otherwise.

## Status Icons

| Icon | Status | Meaning |
|------|--------|---------|
| 🆕 | New | Not yet started |
| 🔄 | In Progress | Work underway |
| ✅ | Done | Completed and verified |
| ❌ | Blocked | Cannot proceed — blocker noted |
| ⏭️ | Deferred | Pushed to a future date |

## Priority Colour Coding

| Code | Level | Meaning |
|------|-------|---------|
| 🔴 | Priority 1 | Must be done today, time-sensitive or blocking |
| 🟡 | Priority 2 | Important but not urgent |
| 🟢 | Priority 3 | Nice to have, can defer if needed |
| 🟠 | Priority 4+ | Backlog / stretch goals |

## AI Workforce Delegation (Sentient context)

When a task belongs to a specific domain, note the delegate in the Delegate field. This is for tracking only — Claude executes all tasks directly. If working outside the Sentient root and delegation doesn't apply, omit the Delegate field.

| Domain | Delegate |
|--------|----------|
| Email, calendar, admin | Vivien (PA) |
| Financial tasks | Eddie (CFO) |
| Sales-related | Donny (Sales) |
| Marketing/collateral | Mary (Marketing) |
| Project management | Cedric (Projects) |
| Development/technical | Alex (Dev) |
| Cross-functional | N/A (cross-functional) |

---

## Operation: CREATE

**Purpose:** Build a new daily plan file with tasks organised by priority, plus a shell audit file.

### Steps

1. **Check for an existing plan today.** If a plans file already exists with tasks, do **not** offer to append new tasks to it — that is the **NEW** sub-command's responsibility. Instead, let the user know a plan already exists and ask if they want to **replace** it entirely. If yes, overwrite it. If no, stop and suggest using `new task` to add individual items.

2. **Gather tasks.** If the user has provided a task list, use it. If they said "plan my day" without specifics, ask what tasks they want planned.

3. **Organise by priority.** Group tasks into priority levels (🔴 P1, 🟡 P2, 🟢 P3, etc.). If priorities aren't specified, suggest a grouping and ask for confirmation. Assign sequential task numbers within each group (e.g., 1.1, 1.2 for P1; 2.1, 2.2 for P2).

4. **Write the plans file** using this template:

```markdown
# Daily Plan — DD Month YYYY

**Date:** YYYY-MM-DD

### Status Legend
| Icon | Status | Meaning |
|------|--------|---------|
| 🆕 | New | Not yet started |
| 🔄 | In Progress | Work underway |
| ✅ | Done | Completed and verified |
| ❌ | Blocked | Cannot proceed |
| ⏭️ | Deferred | Pushed to future date |

---

## Status of Previous Plans

| Item | Status | Notes |
|------|--------|-------|
| (carry-forward items or "No carry-forward items") | | |

---

## Today's Tasks

### 🔴 Priority 1: [Category Name]

#### 1.1 🆕 [Task title]
- **Action:** What Claude should do (be specific — tool, target, output)
- **Delegate:** [AI Workforce member name, or N/A]
- **Effort:** ~N mins

(repeat for each task)

---

## Estimated Total Effort

| Priority | Items | Estimated Time |
|----------|-------|---------------|
| 🔴 P1 | N | ~X mins |
| 🟡 P2 | N | ~X mins |
| 🟢 P3 | N | ~X mins |
| **Total** | **N** | **~X mins** |
```

5. **Create the audit shell:**

```markdown
# Daily Plan Audit — DD Month YYYY

---
```

6. **Present the plan summary** — a compact table showing task numbers, titles, priorities, and effort estimates. Ask for approval before considering the plan final.

> **Scope boundary:** CREATE is only for initialising a brand-new plan. It does not add tasks to an existing plan. Use the **NEW** sub-command for that.

---

## Operation: NEW

**Purpose:** Add a single new task to today's existing plan.

### Steps

1. **Read today's plans file.** If none exists, offer to create one with CREATE instead.

2. **Gather task details.** The user may supply the full task inline (e.g., "add task: Review pitch deck — P1, ~10 mins") or just a title. If any required field is missing, ask:
   - Task title (required)
   - Action description — what Claude should actually do (required)
   - Priority level — 🔴 P1 / 🟡 P2 / 🟢 P3 / 🟠 P4+ (default: 🟡 P2 if not specified)
   - Delegate — AI Workforce member or N/A (optional; omit if not in Sentient context)
   - Effort estimate, e.g. `~10 mins` (optional; omit if unknown)

3. **Determine the task number.** Find the highest existing task number in the chosen priority group and increment by 1. If the priority group does not yet exist, create it with task number X.1 (e.g., new P2 group starts at 2.1).

4. **Add the task block** to the plans file in the correct priority group using this format:

```markdown
#### N.N 🆕 [Task title]
- **Action:** [What Claude should do]
- **Delegate:** [Name or N/A]
- **Effort:** ~N mins
```

5. **Update the Estimated Total Effort table** — increment the item count and time for the affected priority level and the totals row.

6. **Present a confirmation** — show the newly added task and the updated effort summary.

---

## Operation: EXECUTE

**Purpose:** Execute exactly **one task** from today's plan, then stop and report back.

The user triggers each task individually. This skill never loops through multiple tasks in a single invocation — the user wants full control over pacing and may want to review output, pivot, re-prioritise, or handle something else between tasks.

### Steps

1. **Read the plans file.** If no plan exists, tell the user and offer to create one.

2. **First invocation only — show the task summary.** If all tasks are still 🆕, show a compact status table of all tasks grouped by priority, then proceed to execute the first one.

3. **Find the next actionable task.** Scan top-to-bottom by priority for the first task marked 🆕. Skip ✅, ❌, and ⏭️. If none remain, report that all tasks are complete and show a completion summary.

4. **Execute that single task.** Do whatever the Action field specifies — email, calendar, Drive, document creation, web search, or any available tool.

5. **Update the plans file:**
   - Change the task icon from 🆕 to ✅ (or ❌ if blocked, ⏭️ if deferred)
   - If all tasks in a priority group are now complete, append `✅ Done` to the priority heading

6. **Write the audit entry:**

```markdown
## [Task Number] [Task Name]
**Status:** ✅ Done
**Action Taken:** One sentence describing what was executed.
**Output:** Link to file, summary of result, or confirmation of action taken.
**Verification:**
- [x] Specific thing that was verified
- [x] Another verification item
```

Each task gets its own `##` heading — never group multiple tasks. The Output field must include a concrete deliverable. Verification items should be specific and checked.

7. **Report and stop.** Tell the user what was done and what the output was. Briefly mention the next pending task (if any). Then **stop** — do not proceed to the next task. Wait for an explicit "next task", "continue", or "execute" trigger.

---

## Operation: LOG

**Purpose:** Record a just-completed task in today's plans and audit files retroactively — for tasks completed conversationally outside the formal plan execution flow.

### Steps

1. **Identify the task.** Look at the conversation history for the most recent task that was completed. If ambiguous, ask which task to log.

2. **Read or create today's plans file.** If none exists, create one using the standard template.

3. **Add the task** with ✅ Done status in the appropriate priority group. Default to 🟡 Priority 2 if priority is unclear. Use the next available task number.

4. **Write the audit entry** (create the audit file if needed):

```markdown
## [N.N] [Task Name]
**Status:** ✅ Done
**Action Taken:** One sentence describing what was executed.
**Output:** Link to deliverable, summary of result, or confirmation.
**Verification:**
- [x] Specific thing that was verified
- [x] Another verification item
```

5. **Confirm** that the task has been logged in both files.

---

## Operation: STATUS

**Purpose:** Show a quick summary of today's plan progress.

### Steps

1. **Read the plans file.** If none exists, report that and offer to create one.

2. **Present a summary table** grouped by priority:

| # | Task | Status | Effort |
|---|------|--------|--------|
| 1.1 | Task title | ✅ Done | ~5 mins |
| 1.2 | Task title | 🆕 New | ~10 mins |
| 2.1 | Task title | 🔄 In Progress | ~15 mins |

3. **Include totals:**

| | Completed | Remaining | Blocked/Deferred |
|---|---|---|---|
| **Count** | X | Y | Z |
| **Effort** | ~N mins | ~N mins | ~N mins |

4. If there are blocked or deferred tasks, briefly note the reason for each.

---

## Operation: DELETE

**Purpose:** Remove a specified task from today's plan and renumber the remaining tasks so there are no gaps.

### Steps

1. **Read the plans file.** If none exists, report there's no plan to edit.

2. **Identify the task to delete.** The user will reference it by number (e.g., "delete task 2.1"), by name, or by description. If ambiguous, show a numbered list and ask which to remove.

3. **Confirm before deleting.** Show the task that will be removed and ask for confirmation.

4. **Remove the task** entirely — the full `#### N.N` block including Action, Delegate, and Effort lines.

5. **Renumber remaining tasks within the same priority group.** Tasks must stay sequential with no gaps. Tasks in other priority groups are unaffected.

6. **Handle empty priority groups.** If the deletion leaves a priority group with zero tasks, remove the entire priority heading.

7. **Update the Estimated Total Effort table** — adjust item count and time for the affected priority level and the totals row.

8. **Present the updated plan** — a compact summary table of remaining tasks for verification.

### Renumbering example

Before deleting task 1.2:
```
#### 1.1 🆕 Draft BeeNext reply
#### 1.2 🆕 Review pitch deck        ← deleted
#### 1.3 🆕 Send Cap Vista pack
```

After:
```
#### 1.1 🆕 Draft BeeNext reply
#### 1.2 🆕 Send Cap Vista pack      ← was 1.3, now 1.2
```

Cross-priority numbering stays independent — deleting a P1 task does not affect P2 or P3 numbering.

---

## Operation: CARRY-FORWARD

**Purpose:** Pull incomplete tasks from a previous day's plan into today's plan.

### Steps

1. **Find the most recent previous plan.** Look for the latest plans file earlier than today.

2. **Extract incomplete tasks.** Collect all tasks marked ❌ (Blocked) or ⏭️ (Deferred). Ignore ✅ (Done).

3. **Check if today's plan exists:**
   - If yes, add carried-forward items to the "Status of Previous Plans" table
   - If no, create today's plan file with those items in the status section

4. **Present what was carried forward** — a table with original status and any notes about why they were blocked/deferred.

5. **Ask the user** whether to re-add them as active tasks in today's plan or just track them in the status section.

---

## Edge Cases

- **No plan file exists and user says "execute":** Report there's no plan yet and offer to create one.
- **All tasks already done and user says "execute":** Confirm everything is complete. Offer to add more tasks.
- **Multiple plans files for the same date:** Use the most recently modified one.
- **User says "skip" during execution:** Mark the task as ⏭️ Deferred with a note "Skipped by user" and report back.
- **User says "block" or identifies a blocker:** Mark the task as ❌ Blocked, note the blocker, and report back.
- **Task takes longer than expected:** Complete it and report the actual outcome. Don't update effort estimates retroactively.
- **Deleting a completed task:** Allow it but warn that the audit entry will remain (audit entries are never deleted).
