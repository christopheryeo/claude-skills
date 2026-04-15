---
name: daily-plans
description: >
  Manages a daily task planning system using Plans/ in whatever folder is currently selected — creating plans, adding new tasks, executing tasks one-by-one, logging completed work, checking status, deleting tasks, and carrying forward incomplete items. Works from any mounted folder. Seven operations: CREATE, NEW, EXECUTE (one task per invocation), LOG, STATUS, DELETE (with auto-renumbering), CARRY-FORWARD. Use whenever the user says "plan my day", "create a plan", "new task", "add a task", "add task [X]", "execute the plan", "next task", "log task", "log that", "plan status", "what's the plan", "where are we", "carry forward", "carry over", "delete task", "remove task", "drop task", or provides a numbered task list. Do NOT trigger for "set up my workday", "what did I do today?", meeting prep, email drafting, or calendar searches.
---

# Daily Plans

A unified daily task planning system with seven operations: **create**, **new**, **execute**, **log**, **status**, **delete**, and **carry-forward**. Plans are stored as date-stamped entries inside a **journal file** (`Journals/YYYY-MM Plans.md`), using the same structure defined by the `daily-journals` skill. Completion evidence (output links and verification checklists) is recorded inline within each task block.

---

## Token Optimisation Rules

These rules reduce file size and token consumption. Follow them strictly when writing or updating plan entries.

1. **No per-day Status Legend.** The Status Legend table is defined once in this skill and optionally once at the top of each monthly Plans journal file. Never repeat it inside individual daily entries.
2. **No empty-day boilerplate.** If a day has zero tasks (no carry-forward items, no scheduled work), write only a collapsed one-liner: `## YYYY-MM-DD — No tasks`. Do not generate Morning Routine, Status of Previous Plans, Today's Tasks, or Estimated Total Effort sections for empty days.
3. **Inline effort for single-task days.** If a day has exactly 1 task, replace the full Estimated Total Effort table with a single line: `**Effort:** ~N mins (1 task, PX)`.

---

## Dependency: daily-journals

This skill depends on the **daily-journals** skill for plan storage. Plan content is written as journal entries inside `Journals/YYYY-MM Plans.md`, where each day's plan sits under a `## YYYY-MM-DD` date header in reverse-chronological order (newest first).

The following daily-journals sub-commands are used:

| daily-plans operation | Calls | Which calls | Purpose |
|---|---|---|---|
| **CREATE** | — | daily-journals **CREATE-JOURNAL** | Ensure `Journals/YYYY-MM Plans.md` exists (purpose: "Plans") |
| **CREATE** | — | daily-journals **CREATE-ENTRY** | Insert the full plan content under a new `## YYYY-MM-DD` date header |
| **NEW** | — | daily-journals **CREATE-ENTRY** | Append a new task block into today's existing `## YYYY-MM-DD` entry |
| **LOG** | daily-plans **NEW** | daily-journals **CREATE-ENTRY** (via NEW) | Add an already-completed (✅) task to today's plan with inline Output and Verification fields |

All other sub-commands (EXECUTE, STATUS, DELETE, CARRY-FORWARD) read and write today's plan by locating the `## YYYY-MM-DD` entry for the relevant date inside the current month's Plans journal.

---

## Locating Files

This skill is **folder-agnostic** — it works from whatever folder the user has selected (mounted).

1. **Determine the mounted root.** The user's selected workspace is the mount point (e.g., `/sessions/.../mnt/Sentient`, `/sessions/.../mnt/Mary (Marketing)`, etc.).
2. **Journals/ folder** — used for plan content. Follow the daily-journals skill's folder resolution: look for `Journals/` at the mounted root; create it if missing.

Never hardcode a specific parent folder.

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

- **Plans journal:** `Journals/YYYY-MM Plans.md` — plan content lives as an entry under the `## YYYY-MM-DD` date header for the relevant day.

Use today's date unless the user specifies otherwise. When reading "today's plan", open `Journals/YYYY-MM Plans.md` and find the `## YYYY-MM-DD` section matching today's date.

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

**Purpose:** Build a new daily plan as a journal entry inside `Journals/YYYY-MM Plans.md`.

### Steps

1. **Ensure the Plans journal exists.** Invoke the daily-journals **CREATE-JOURNAL** logic with purpose **"Plans"** and the current month. This checks for `Journals/YYYY-MM Plans.md` — if it exists, use it; if not, create it. (Do not prompt the user for the purpose — it is always "Plans".)

2. **Check for an existing plan today.** Read the Plans journal and look for a `## YYYY-MM-DD` header matching today's date. If an entry already exists with tasks, do **not** offer to append new tasks to it — that is the **NEW** sub-command's responsibility. Instead, let the user know a plan already exists and ask if they want to **replace** it entirely. If yes, remove the existing date section and rewrite it. If no, stop and suggest using `new task` to add individual items.

3. **Gather tasks.** If the user has provided a task list, use it. If they said "plan my day" without specifics, ask what tasks they want planned.

4. **Organise by priority.** Group tasks into priority levels (🔴 P1, 🟡 P2, 🟢 P3, etc.). If priorities aren't specified, suggest a grouping and ask for confirmation. Assign sequential task numbers within each group (e.g., 1.1, 1.2 for P1; 2.1, 2.2 for P2).

5. **Write the plan as a journal entry.** Using the daily-journals **CREATE-ENTRY** insertion logic, add the plan content under a `## YYYY-MM-DD` date header in the Plans journal. The entry is inserted in reverse-chronological order (newest first). The content beneath the date header uses this template:

```markdown
### Daily Plan — DD Month YYYY

#### Status of Previous Plans

| Item | Status | Notes |
|------|--------|-------|
| (carry-forward items or "No carry-forward items") | | |

---

#### Today's Tasks

##### 🔴 Priority 1: [Category Name]

###### 1.1 🆕 [Task title]
- **Action:** What Claude should do (be specific — tool, target, output)
- **Delegate:** [AI Workforce member name, or N/A]
- **Effort:** ~N mins

(repeat for each task)

---

#### Estimated Total Effort

| Priority | Items | Estimated Time |
|----------|-------|---------------|
| 🔴 P1 | N | ~X mins |
| 🟡 P2 | N | ~X mins |
| 🟢 P3 | N | ~X mins |
| **Total** | **N** | **~X mins** |
```

> **No Status Legend in daily entries.** The legend is defined once in this skill file and optionally once at the top of the monthly journal. Do not include it in each day's plan.

> **Single-task days:** If the plan has only 1 task, replace the Estimated Total Effort table with: `**Effort:** ~N mins (1 task, PX)`.

> **Heading levels:** Because the plan sits inside a journal entry (under a `## YYYY-MM-DD` header), all internal headings are shifted down by two levels compared to the old standalone format: `#` → `###`, `##` → `####`, `###` → `#####`, `####` → `######`.

6. **Present the plan summary** — a compact table showing task numbers, titles, priorities, and effort estimates. Ask for approval before considering the plan final.

> **Scope boundary:** CREATE is only for initialising a brand-new plan. It does not add tasks to an existing plan. Use the **NEW** sub-command for that.

---

## Operation: NEW

**Purpose:** Add a single new task to today's existing plan entry in the Plans journal, using the daily-journals **CREATE-ENTRY** sub-command to write the task content.

### Steps

1. **Read today's plan entry.** Open `Journals/YYYY-MM Plans.md` and locate the `## YYYY-MM-DD` section for today. If no entry exists for today, offer to create one with CREATE instead.

2. **Gather task details.** The user may supply the full task inline (e.g., "add task: Review pitch deck — P1, ~10 mins") or just a title. If any required field is missing, ask:
   - Task title (required)
   - Action description — what Claude should actually do (required)
   - Priority level — 🔴 P1 / 🟡 P2 / 🟢 P3 / 🟠 P4+ (default: 🟡 P2 if not specified)
   - Delegate — AI Workforce member or N/A (optional; omit if not in Sentient context)
   - Effort estimate, e.g. `~10 mins` (optional; omit if unknown)

3. **Determine the task number.** Find the highest existing task number in the chosen priority group and increment by 1. If the priority group does not yet exist, create it with task number X.1 (e.g., new P2 group starts at 2.1).

4. **Add the task using CREATE-ENTRY.** Invoke the daily-journals **CREATE-ENTRY** sub-command to insert the new task block into today's `## YYYY-MM-DD` entry in `Journals/YYYY-MM Plans.md`. CREATE-ENTRY handles locating the correct date header and appending content beneath it. The task block to insert uses this format:

```markdown
###### N.N 🆕 [Task title]
- **Action:** [What Claude should do]
- **Delegate:** [Name or N/A]
- **Effort:** ~N mins
```

> **Placement within the entry:** Unlike a standard journal entry where CREATE-ENTRY appends below existing content under the date header, the task block must be inserted into the correct **priority group** within today's plan entry. Locate the matching `##### 🔴/🟡/🟢/🟠 Priority N` heading inside the date section and append the task block after the last existing task in that group. If the priority group does not yet exist, create the heading and task block before the `#### Estimated Total Effort` section.

5. **Update the Estimated Total Effort table** within today's entry — increment the item count and time for the affected priority level and the totals row. If the day previously had 0 tasks (collapsed one-liner `## YYYY-MM-DD — No tasks`), expand it into the full CREATE template first.

6. **Present a confirmation** — show the newly added task and the updated effort summary.

---

## Operation: EXECUTE

**Purpose:** Execute exactly **one uncompleted task** from today's plan, update its status to done, then stop. Only one task is executed per invocation — never more.

### Constraint: One Task Per Invocation

This skill executes **a single task per call** and then stops. It never loops through multiple tasks, never auto-advances to the next task, and never batches work. The user controls the pace and decides when to trigger the next task by saying "next task", "continue", or "execute" again.

### Steps

1. **Open the Plans journal and find today's entry.** Read `Journals/YYYY-MM Plans.md` and locate the `## YYYY-MM-DD` section matching today's date. If no entry exists for today, tell the user and offer to create one via the CREATE operation. If the journal file itself does not exist, report that and stop.

2. **Scan today's entry for the first uncompleted task.** Starting from the highest-priority group (🔴 P1) and working down (🟡 P2 → 🟢 P3 → 🟠 P4+), read each task heading (`###### N.N`) in order and check its status icon:
   - **🆕 (New)** or **🔄 (In Progress)** → this is the task to execute. Stop scanning.
   - **✅ (Done)** → skip, already completed.
   - **❌ (Blocked)** → skip, cannot proceed.
   - **⏭️ (Deferred)** → skip, pushed to a future date.

   If **every task** in today's entry is ✅, ❌, or ⏭️ (i.e., no uncompleted tasks remain), report that all tasks are complete, show a completion summary, and stop. Do not execute anything.

3. **First invocation only — show the full task summary.** If this is the first EXECUTE call of the session (all actionable tasks are still 🆕), present a compact status table of all tasks grouped by priority before executing, so the user can see the full plan at a glance.

4. **Execute that single task.** Perform whatever the task's **Action** field specifies — email, calendar, Drive, document creation, web search, or any available tool. Complete the work fully before proceeding to the next step.

5. **Update the task's status in the Plans journal.** Re-open `Journals/YYYY-MM Plans.md`, locate today's `## YYYY-MM-DD` entry, find the specific `###### N.N` heading for the task just executed, and change its status icon:
   - **🆕 → ✅** if the task completed successfully
   - **🆕 → ❌** if a blocker was encountered (note the blocker)
   - **🆕 → ⏭️** if the user said "skip" (note "Skipped by user")

   Then check whether all tasks in that priority group are now ✅ — if so, append `✅ Done` to the priority group heading (`##### 🔴/🟡/🟢/🟠 Priority N`).

6. **Append completion evidence to the task block.** Re-open `Journals/YYYY-MM Plans.md`, locate today's `## YYYY-MM-DD` entry, find the specific `###### N.N` heading for the task just executed, and append **Output** and **Verification** fields below the existing Action/Delegate/Effort lines:

```markdown
###### 1.1 ✅ [Task title]
- **Action:** What was done
- **Delegate:** Name
- **Effort:** ~N mins
- **Output:** Link to deliverable, summary of result, or confirmation
- **Verification:**
  - [x] Specific thing verified
  - [x] Another verification item
```

The Output field must include a concrete deliverable. Verification items should be specific and checked.

7. **Report and stop.** Tell the user:
   - What task was executed (number and title)
   - What the output/result was
   - What the next uncompleted task is (number, title, and priority), or confirm that all tasks are now done

   Then **stop**. Do not proceed to the next task. Wait for an explicit "next task", "continue", or "execute" trigger from the user before running EXECUTE again.

---

## Operation: LOG

**Purpose:** Record a just-completed task in today's plan entry retroactively — for tasks completed conversationally outside the formal plan execution flow. LOG delegates to the **NEW** sub-command to create the task entry, but with ✅ Done status instead of 🆕 New, and includes inline Output and Verification fields.

### Steps

1. **Identify the task.** Look at the conversation history for the most recent task that was completed. If ambiguous, ask which task to log.

2. **Derive task details from the conversation.** Extract the following from what was just completed:
   - Task title (required) — a concise name for what was done
   - Action description (required) — what was actually performed
   - Priority level — default to 🟡 P2 if unclear from context
   - Delegate — infer from the domain if in Sentient context, otherwise omit
   - Effort estimate — estimate based on conversation duration/complexity, or omit if unknown

3. **Invoke the NEW sub-command** to add the task to today's plan entry. NEW handles all journal interaction: ensuring today's `## YYYY-MM-DD` entry exists in `Journals/YYYY-MM Plans.md` (falling back to CREATE if needed), determining the next task number, inserting the task block into the correct priority group via CREATE-ENTRY, and updating the Estimated Total Effort table. The only difference from a normal NEW invocation is:
   - The task icon is **✅** (Done) instead of 🆕 (New)
   - The task block is written as:

```markdown
###### N.N ✅ [Task title]
- **Action:** [What was done]
- **Delegate:** [Name or N/A]
- **Effort:** ~N mins
```

4. **Append completion evidence to the task block.** Since LOG writes the task as ✅ via NEW, the Output and Verification fields are included in the initial task block:

```markdown
###### N.N ✅ [Task title]
- **Action:** What was done
- **Delegate:** Name or N/A
- **Effort:** ~N mins
- **Output:** Link to deliverable, summary of result, or confirmation
- **Verification:**
  - [x] Specific thing verified
  - [x] Another verification item
```

5. **Confirm** that the task has been logged in the Plans journal with verification.

---

## Operation: STATUS

**Purpose:** Show a quick summary of today's plan progress, with an optional filter to show only tasks of a specific status.

### Optional Status Filter

The user may request a filtered view by specifying a status in their trigger phrase. Recognised filter phrases and their mappings:

| Trigger phrase | Filter applied |
|---|---|
| "show new tasks", "what's new", "show pending" | 🆕 New only |
| "show in progress", "what's in progress", "what's underway" | 🔄 In Progress only |
| "show done", "what's done", "what's completed" | ✅ Done only |
| "show blocked", "what's blocked", "any blockers" | ❌ Blocked only |
| "show deferred", "what's deferred", "what's postponed" | ⏭️ Deferred only |
| "plan status", "what's the plan", "show plan", "where are we" (no qualifier) | All tasks (no filter) |

If a filter is detected, note it at the top of the response (e.g., *Showing: 🆕 New tasks only*).

### Steps

1. **Read today's plan entry.** Open `Journals/YYYY-MM Plans.md` and locate the `## YYYY-MM-DD` section for today. If no entry exists, report that and offer to create one. If the entry is a collapsed one-liner (`## YYYY-MM-DD — No tasks`), report that no tasks are planned.

2. **Apply the filter (if any).** If the user specified a status filter, restrict the displayed tasks to only those matching that status. If no filter was given, include all tasks regardless of status.

3. **Present a summary table** grouped by priority (omit priority groups with no matching tasks when a filter is active):

| # | Task | Status | Effort |
|---|------|--------|--------|
| 1.1 | Task title | ✅ Done | ~5 mins |
| 1.2 | Task title | 🆕 New | ~10 mins |
| 2.1 | Task title | 🔄 In Progress | ~15 mins |

If no tasks match the active filter, report: *"No tasks found with status [filter] in today's plan."*

4. **Include totals** (always based on the full plan, not the filtered view — label clearly):

| | Completed | Remaining | Blocked/Deferred |
|---|---|---|---|
| **Count** | X | Y | Z |
| **Effort** | ~N mins | ~N mins | ~N mins |

5. If there are blocked or deferred tasks (in the full plan), briefly note the reason for each.

---

## Operation: DELETE

**Purpose:** Remove a specified task from today's plan and renumber the remaining tasks so there are no gaps.

### Steps

1. **Read today's plan entry.** Open `Journals/YYYY-MM Plans.md` and locate the `## YYYY-MM-DD` section for today. If no entry exists, report there's no plan to edit.

2. **Identify the task to delete.** The user will reference it by number (e.g., "delete task 2.1"), by name, or by description. If ambiguous, show a numbered list and ask which to remove.

3. **Confirm before deleting.** Show the task that will be removed and ask for confirmation.

4. **Remove the task** entirely — the full `###### N.N` block including Action, Delegate, and Effort lines.

5. **Renumber remaining tasks within the same priority group.** Tasks must stay sequential with no gaps. Tasks in other priority groups are unaffected.

6. **Handle empty priority groups.** If the deletion leaves a priority group with zero tasks, remove the entire priority heading.

7. **Update the Estimated Total Effort table** — adjust item count and time for the affected priority level and the totals row. If the plan now has 0 tasks, collapse the entire day to `## YYYY-MM-DD — No tasks`. If exactly 1 task remains, replace the effort table with the inline format.

8. **Present the updated plan** — a compact summary table of remaining tasks for verification.

### Renumbering example

Before deleting task 1.2:
```
###### 1.1 🆕 Draft BeeNext reply
###### 1.2 🆕 Review pitch deck        ← deleted
###### 1.3 🆕 Send Cap Vista pack
```

After:
```
###### 1.1 🆕 Draft BeeNext reply
###### 1.2 🆕 Send Cap Vista pack      ← was 1.3, now 1.2
```

Cross-priority numbering stays independent — deleting a P1 task does not affect P2 or P3 numbering.

---

## Operation: CARRY-FORWARD

**Purpose:** Pull incomplete tasks from **yesterday's** plan entry into today's plan.

### Steps

1. **Find yesterday's plan entry.** Calculate yesterday's date and open `Journals/YYYY-MM Plans.md`. Locate the `## YYYY-MM-DD` entry matching yesterday's date. If no entry exists for yesterday (including collapsed `— No tasks` entries), inform the user that there is no previous day's plan to carry forward and stop.

2. **Extract incomplete tasks.** From yesterday's entry only, collect all tasks marked ❌ (Blocked) or ⏭️ (Deferred). Ignore ✅ (Done). If no incomplete tasks are found, inform the user and stop.

3. **Check if today's plan entry exists:**
   - If yes, add carried-forward items to the "Status of Previous Plans" table within today's entry
   - If it's a collapsed one-liner (`— No tasks`), expand it into the full CREATE template first
   - If no, create today's plan entry using the CREATE operation, with those items in the status section

4. **Present what was carried forward** — a table with original status and any notes about why they were blocked/deferred.

5. **Ask the user** whether to re-add them as active tasks in today's plan or just track them in the status section.

---

## Edge Cases

- **No plan entry exists for today and user says "execute":** Report there's no plan yet and offer to create one.
- **No Plans journal exists at all:** Invoke CREATE-JOURNAL logic to create `Journals/YYYY-MM Plans.md` before proceeding.
- **All tasks already done and user says "execute":** Confirm everything is complete. Offer to add more tasks.
- **Yesterday has no plan entry:** CARRY-FORWARD reports that no previous day's plan was found and stops — it does not search further back.
- **Yesterday falls in a different month (e.g., 1st of the month):** Open the prior month's Plans journal (e.g., `Journals/2026-02 Plans.md`) to find yesterday's entry. Only yesterday's date is checked — no broader scan.
- **User says "skip" during execution:** Mark the task as ⏭️ Deferred with a note "Skipped by user" and report back.
- **User says "block" or identifies a blocker:** Mark the task as ❌ Blocked, note the blocker, and report back.
- **Task takes longer than expected:** Complete it and report the actual outcome. Don't update effort estimates retroactively.
- **Deleting a completed task:** Allow it but confirm first, as the verification record will also be removed.
- **Editing another day's plan:** If the user asks to modify a past day's plan, locate the correct `## YYYY-MM-DD` entry in the Plans journal. This is supported but uncommon — confirm the date with the user before editing.
- **Collapsed one-liner encountered during NEW/CARRY-FORWARD:** If today's entry is `## YYYY-MM-DD — No tasks`, expand it into the full CREATE template before inserting tasks.
