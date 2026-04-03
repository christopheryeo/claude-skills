---
name: daily-JIRA
description: >
  Daily JIRA companion for the Sentient Workforce project (SMTC). Seven sub-commands: TEAM ISSUES (all open issues assigned to any team member including me, grouped by assignee and status), SPRINT (current sprint board with progress and blockers), STORIES BY EPIC (stories grouped under each epic with progress bars), SUBTASKS (sub-tasks under a specific story), ISSUE DETAIL (full detail card for any story or sub-task — status, title, description, due date, assignee), CREATE (guided issue creation), and UPDATE (transition status, add comments, edit fields). Use whenever the user says "team issues", "what's the team working on", "team's jira", "show the sprint", "sprint status", "sprint board", "stories by epic", "epic breakdown", "subtasks for", "show subtasks", "issue detail", "show me SMTC-", "what's the status of", "create a jira issue", "log a bug", "new story", "update issue", "transition", "add a comment to", "close issue", "move to done", or any request involving JIRA tasks, sprints, or tickets for Sentient Workforce. Always use this skill for JIRA-related requests — do not handle them ad hoc.
---

# Daily JIRA

A daily JIRA companion for the **Sentient Workforce** project on `sentient-smartchat.atlassian.net`.

## Connection Details

| Field | Value |
|---|---|
| **Site** | sentient-smartchat.atlassian.net |
| **Cloud ID** | 4483a4d2-748f-44a8-9251-c7fa634335e7 |
| **Project** | Sentient workforce |
| **Project Key** | SMTC |
| **Issue Types** | Epic · Story · Task · Bug · Subtask |

---

## Connector Policy

**Always use the native Atlassian connector first.** Only fall back to the Zapier JIRA connector if the native connector fails, returns an error, or cannot perform the specific operation.

### Native Atlassian Connector (primary)

Use these tools by default for every sub-command:

| Operation | Tool | Notes |
|---|---|---|
| Search / JQL queries | `searchJiraIssuesUsingJql` | **Do NOT pass the `fields` parameter** — it is broken in this runtime (see below). Use bare JQL only. |
| Fetch single issue (full detail) | `getJiraIssue` | Use parameter name `issueIdOrKey`. Returns assignee, duedate, subtasks, sprint, parent — use this whenever those fields are needed. |
| Create issue | `createJiraIssue` | — |
| Edit issue fields | `editJiraIssue` | — |
| Transition status | `transitionJiraIssue` | — |
| Get available transitions | `getTransitionsForJiraIssue` | — |
| Add comment | `addCommentToJiraIssue` | — |
| Current user info | `atlassianUserInfo` | — |
| Look up user account ID | `lookupJiraAccountId` | — |
| Fetch by ARI | `fetchAtlassian` | Requires an ARI (`id` param), e.g. `ari:cloud:jira:4483a4d2-...:issue/14146` — not a URL path. |

#### Known tool limitation — `fields` parameter

`searchJiraIssuesUsingJql` has a `fields` parameter typed as a JSON array, but the runtime serialises it as a string, which the MCP server rejects. **Always omit `fields`.** The default payload returns: summary, issuetype, priority, status, description — but **not** assignee or duedate.

To get assignee, duedate, sprint, subtasks, or parent for a set of issues, call `getJiraIssue` (with `issueIdOrKey`) on each issue key individually after the JQL search. This is the correct pattern for all sub-commands that need those fields.

### Zapier JIRA Connector (fallback only)

Use the `jira_software_cloud_*` tools **only** if the native connector throws an error or lacks the required capability. When falling back, note it briefly (e.g. *"Using fallback connector"*).

> **Important:** Zapier tools require a natural language `instructions` parameter in addition to their query parameters. Always pass `instructions` describing the task, e.g. `"Find all open issues in project SMTC assigned to the team"`.

| Operation | Fallback Tool |
|---|---|
| Search / JQL queries | `jira_software_cloud_find_issues_via_jql` |
| Fetch single issue | `jira_software_cloud_find_issue_by_key` |
| Create issue | `jira_software_cloud_create_issue` |
| Edit issue fields | `jira_software_cloud_update_issue` |
| Add comment | `jira_software_cloud_add_comment_to_issue` |
| Sprint info | `jira_software_cloud_get_sprint_information` |
| Move to sprint | `jira_software_cloud_move_issue_to_sprint` |

Always scope queries to project = SMTC unless the user specifies otherwise.

---

## Detecting the Sub-Command

| Trigger | Sub-command |
|---|---|
| "team issues", "what's the team working on", "team's jira", "team tickets" | **TEAM ISSUES** |
| "sprint", "sprint board", "sprint status", "show the board", "what's in the sprint" | **SPRINT** |
| "by epic", "epic status", "stories by epic", "epic breakdown", "stories under" | **STORIES BY EPIC** |
| "subtasks for", "show subtasks", "subtasks under", "tasks in story" | **SUBTASKS** |
| "issue detail", "show me SMTC-", "what's the status of", "detail for", "tell me about SMTC-" | **ISSUE DETAIL** |
| "create issue", "new ticket", "log a bug", "new story", "new task", "create a jira" | **CREATE** |
| "update issue", "transition", "close issue", "move to done", "add a comment", "edit issue" | **UPDATE** |

If the intent is ambiguous, ask which sub-command the user means. Usually context makes it obvious.

---

## Output Conventions

### Issue Table Format

Use this format whenever listing issues:

| Key | Type | Summary | Status | Priority | Assignee | Due |
|---|---|---|---|---|---|---|
| [SMTC-42](https://sentient-smartchat.atlassian.net/browse/SMTC-42) | 🐛 Bug | Fix login timeout | 🔵 In Progress | 🔴 High | Chris | 2026-04-10 |

**Type icons:** 🗂 Epic · 📖 Story · ✅ Task · 🐛 Bug · 🔹 Subtask

**Status colours:**
- ⚪ To Do
- 🔵 In Progress
- 🟢 Done
- 🔴 Blocked
- 🟡 In Review

**Priority icons:** 🔴 Highest/High · 🟡 Medium · 🟢 Low/Lowest

Always hyperlink issue keys to `https://sentient-smartchat.atlassian.net/browse/[KEY]`.

If a due date is not set, show `—` in the Due column.

**Column no-wrap rule:** The `Key`, `Status`, and `Due` columns must never word-wrap. Use these exact conventions:
- **Key:** Use a **non-breaking hyphen** (U+2011 `‑`) instead of a regular hyphen inside the issue key display text, e.g. `[SMTC‑755](https://sentient-smartchat.atlassian.net/browse/SMTC-755)`. The URL itself still uses a regular hyphen; only the visible display text uses `‑`. This prevents the renderer breaking `SMTC-` onto its own line.
- **Status:** Use the **emoji icon only** — no text label — so the cell is always a single character that cannot wrap: `⚪` To Do · `🔵` In Progress · `🟢` Done · `🔴` Blocked · `🟡` In Review. Add a one-line legend above the table: `⚪ To Do · 🔵 In Progress · 🟢 Done · 🔴 Blocked · 🟡 In Review`.
- **Due:** Use compact `DD·Mon` format with a middle dot, e.g. `14·Apr` (no year unless ambiguous). If not set, show `—`.

### Issue Detail Card Format

Use this format for ISSUE DETAIL and whenever showing a single issue in full:

```
─────────────────────────────────────────
📖 [SMTC-42](https://sentient-smartchat.atlassian.net/browse/SMTC-42) — Story
─────────────────────────────────────────
Title:      Fix login timeout on session expiry
Status:     🔵 In Progress
Priority:   🔴 High
Assignee:   Chris Yeo
Due Date:   2026-04-15  (or — if not set)
Sprint:     Sprint 3 (active)  (omit if not in a sprint)

Description:
[Full description text, rendered as plain prose. If empty, show "No description provided."]
─────────────────────────────────────────
```

---

## Sub-Command: TEAM ISSUES

**Purpose:** Surface all open issues assigned to any team member — including Christopher — so he can see the full team workload, identify blockers, and review distribution at a glance.

### Steps

1. **Fetch all open project issues with an assignee** using `searchJiraIssuesUsingJql` (no `fields` parameter):
   ```
   project = SMTC AND assignee is not EMPTY AND statusCategory != Done ORDER BY assignee ASC, priority ASC
   ```

2. **Enrich with full details.** Because `searchJiraIssuesUsingJql` does not return assignee or duedate in its default payload, call `getJiraIssue` (with `issueIdOrKey`) on each returned issue key to get the full fields needed for grouping and display. Batch these calls in parallel where possible.

3. **Group results by assignee.** For each assignee, display a section header followed by their issue table:
   ```
   ### 👤 [Assignee Name] — N open issues
   ```
   Then the standard issue table (Key, Type, Summary, Status, Priority, Due) for that person's issues.

4. **Within each assignee**, order issues: In Progress first, then In Review, then To Do, then Blocked.

5. **Summary at the bottom:**
   > *N team members · X total open issues · Y in progress · Z blocked*

6. If any assignee has **Blocked** issues, flag them with a ❌ note beneath their table.

---

## Sub-Command: SPRINT

**Purpose:** Show the full active sprint board — all issues, progress, and blockers — so Christopher can assess sprint health at a glance.

### Steps

1. **Fetch active sprint issues.** Run JQL:
   ```
   project = SMTC AND sprint in openSprints() ORDER BY status ASC, priority ASC
   ```

2. **Get sprint metadata** (name, start date, end date, goal) using the sprint information API.

3. **Display the sprint header:**
   ```
   ## 🏃 Sprint: [Sprint Name]
   📅 [Start Date] → [End Date]  |  🎯 Goal: [Sprint Goal or "No goal set"]
   ```

4. **Show issues** in the standard issue table (including Due column), grouped by status category:
   - 🔵 **In Progress** (N issues)
   - ⚪ **To Do** (N issues)
   - 🟡 **In Review** (N issues)
   - 🔴 **Blocked** (N issues)
   - 🟢 **Done** (N issues — show count only; list issues only if user asks)

5. **Sprint health summary:**
   | Metric | Value |
   |---|---|
   | Total issues | N |
   | Completed | N (X%) |
   | Remaining | N |
   | Blockers | N |
   | Days remaining | N |

6. If there are **Blocked** issues, call them out explicitly with a brief note on the blocker.

---

## Sub-Command: STORIES BY EPIC

**Purpose:** Show all Stories in the SMTC project grouped under their parent Epics — providing a strategic view of feature-level progress. This sub-command surfaces Stories only (not Tasks, Bugs, or Subtasks).

### Steps

1. **Fetch all open Epics:**
   ```
   project = SMTC AND issuetype = Epic AND statusCategory != Done ORDER BY priority ASC
   ```

2. **For each Epic, fetch its child issues in two attempts:**

   **Attempt A** — Stories only:
   ```
   project = SMTC AND issuetype = Story AND parent = [EPIC-KEY] ORDER BY status ASC, priority ASC
   ```

   **If Attempt A returns 0 results**, some epics in this project use Tasks (not Stories) as direct children. Run **Attempt B** — Stories and Tasks:
   ```
   project = SMTC AND issuetype in (Story, Task) AND parent = [EPIC-KEY] ORDER BY status ASC, priority ASC
   ```

   Use whichever attempt returns results. Note in the epic header which type was found, e.g. *(Tasks)* if only Tasks were returned. This is a known data pattern in the SMTC project — e.g. the Carbon Amber epic uses Tasks as its primary work items.

3. **Also fetch orphaned Stories** (Stories with no parent Epic):
   ```
   project = SMTC AND issuetype = Story AND parent is EMPTY AND "Epic Link" is EMPTY AND statusCategory != Done
   ```

4. **Display one section per Epic:**
   ```
   ### 🗂 [SMTC-XX](link) — [Epic Summary]
   Status: [Epic Status]  |  Priority: [Priority]  |  Progress: ██████░░░░ 6/10 done (60%)
   ```
   Followed by the standard issue table for that epic's stories (Key, Type, Summary, Status, Priority, Assignee, Due).

5. **Orphaned stories** appear at the bottom under:
   ```
   ### ❓ No Epic
   ```

6. **Epic progress bar** counts Done Stories vs. total Stories under that epic.
   > `Progress: ████████░░ 8/10 done (80%)`

---

## Sub-Command: SUBTASKS

**Purpose:** Show all sub-tasks belonging to a specific Story, along with their status, assignee, and due date — useful for checking detailed execution progress within a story.

### Steps

1. **Identify the parent Story.** The user will reference it by key (e.g., SMTC-42) or by name. If by name, search:
   ```
   project = SMTC AND issuetype = Story AND summary ~ "[search term]" ORDER BY updated DESC
   ```
   Show top 3 matches and confirm which story.

2. **Fetch the story's detail first** — display an Issue Detail Card (see Output Conventions) for the parent story so the user has full context.

3. **Fetch its sub-tasks:**
   ```
   project = SMTC AND issuetype = Subtask AND parent = [STORY-KEY] ORDER BY status ASC, priority ASC
   ```

4. **Display the sub-tasks** using the standard issue table (Key, Type, Summary, Status, Priority, Assignee, Due), grouped by status:
   - 🔵 In Progress
   - ⚪ To Do
   - 🟡 In Review
   - 🔴 Blocked
   - 🟢 Done

5. **Summary line:**
   > *X sub-tasks total — Y done, Z remaining*

6. If there are no sub-tasks, say so clearly and offer to create one via the CREATE sub-command.

---

## Sub-Command: ISSUE DETAIL

**Purpose:** Retrieve and display the full details of any Story or Sub-task — including its current status, title, full description, due date, and assignee.

### Steps

1. **Identify the issue.** The user will provide a key (e.g., SMTC-42) or a description. If by description, search:
   ```
   project = SMTC AND summary ~ "[search term]" ORDER BY updated DESC
   ```
   Show top 3 matches and confirm which issue.

2. **Fetch the full issue** using `getJiraIssue` with the issue key. Retrieve at minimum:
   - `summary` (title)
   - `status.name`
   - `priority.name`
   - `assignee.displayName`
   - `description` (full text)
   - `duedate`
   - `issuetype.name`
   - `parent` (if a sub-task or story — to show the parent link)
   - `sprint` (if in an active sprint)

3. **Render the Issue Detail Card** (see Output Conventions format above).

4. **If the issue is a Story**, append a sub-task summary beneath the card:
   > *Sub-tasks: X total — Y done, Z remaining. Say "subtasks for SMTC-XX" to see the full list.*

5. **If the issue is a Sub-task**, show the parent Story link beneath the card:
   > *Parent: [SMTC-XX](link) — [Story title]*

6. **Offer follow-up actions:**
   > *"Would you like to update this issue, add a comment, or see its sub-tasks?"*

---

## Sub-Command: CREATE

**Purpose:** Create a new JIRA issue in the SMTC project with guided prompts.

### Steps

1. **Gather required fields.** If the user has already provided details inline, extract them. Otherwise ask for:
   - **Issue type** — Epic / Story / Task / Bug / Subtask (default: Task)
   - **Summary** — one-line title (required)
   - **Description** — optional, but suggest adding context
   - **Priority** — Highest / High / Medium / Low / Lowest (default: Medium)
   - **Assignee** — default to current user; ask if assigning to someone else
   - **Due date** — optional; ask if the issue has a deadline
   - **Epic link** — if type is Story/Task/Bug, offer to link to an existing Epic (show a short list of open epics)
   - **Sprint** — offer to add to the active sprint (default: yes)

2. **Confirm before creating.** Show a summary card:
   ```
   📋 New Issue Preview
   Type:     [Task]
   Summary:  [Issue title]
   Priority: [Medium]
   Assignee: [Chris]
   Due:      [2026-04-20 or —]
   Epic:     [SMTC-5 — AI Workforce v2]
   Sprint:   [Sprint 3 (active)]
   ```
   Ask: *"Create this issue?"*

3. **Create the issue** using the JIRA create issue API.

4. **On success**, present the new issue key as a link:
   > ✅ Created [SMTC-XX](https://sentient-smartchat.atlassian.net/browse/SMTC-XX) — [Summary]

5. **Offer a follow-up action:** "Would you like to add a description, set a due date, or link this to another issue?"

---

## Sub-Command: UPDATE

**Purpose:** Update an existing SMTC issue — transition its status, add a comment, or edit fields.

### Steps

1. **Identify the issue.** The user may provide a key (e.g., SMTC-42) or describe it by name. If by name, search:
   ```
   project = SMTC AND summary ~ "[search term]" ORDER BY updated DESC
   ```
   Show the top 3 matches and ask the user to confirm which one.

2. **Detect the update type** from the user's phrasing:

   | Intent | Action |
   |---|---|
   | "close", "done", "mark complete", "resolve" | Transition to **Done** |
   | "start", "begin", "move to in progress" | Transition to **In Progress** |
   | "move to review", "submit for review" | Transition to **In Review** |
   | "block", "mark as blocked" | Transition to **Blocked** (or add label) |
   | "comment", "add a note", "log" | Add a comment |
   | "change priority", "reprioritise" | Edit the priority field |
   | "reassign", "assign to" | Edit the assignee field |
   | "rename", "update summary" | Edit the summary field |
   | "set due date", "due by", "deadline" | Edit the due date field |
   | "link to epic" | Set the epic link field |

3. **For transitions:**
   - Fetch available transitions using `getTransitionsForJiraIssue`
   - Map the user's intent to the correct transition ID
   - Execute the transition

4. **For comments:**
   - Compose the comment text (or use the user's exact words)
   - Confirm before posting: *"Post this comment to SMTC-XX?"*
   - Add the comment

5. **Confirm the update:**
   > ✅ SMTC-XX updated — [what changed]

---

## Edge Cases

- **No active sprint:** For the SPRINT sub-command, if no sprint is open, report that and show the backlog instead.
- **Issue not found by name:** If search returns no matches, say so and ask the user to provide the issue key directly.
- **Ambiguous sub-command:** If the user says something like "show me issues" without specifying a filter, default to **TEAM ISSUES**.
- **Creating an Epic:** When issue type is Epic, skip the "Epic Link" field — Epics cannot be children of other Epics.
- **Subtask creation:** Prompt for the parent Story key when creating a Subtask.
- **Permissions error:** If a transition or update is rejected, report the error clearly and suggest checking permissions or issue state.
- **Story with no sub-tasks:** Report clearly and offer to create one.
- **Epic with no stories:** Report "No stories yet" in the STORIES BY EPIC section but still show the epic header.
- **No team members with open issues:** For TEAM ISSUES, report that all team issues are either done or unassigned, then offer to show the backlog.
- **Due date not set:** Always show `—` in the Due column rather than leaving blank or showing `null`.
