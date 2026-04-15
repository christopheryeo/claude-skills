# Claude Skills Library

## Session Startup

At the beginning of every morning working session, read and follow `.claude/startup.md` before doing anything else.

**Project Name:** Claude Skills
**Maintained by:** Chris Yeo
**Version:** 1.36.1 (as of December 2025)

## Overview
This repository contains a collection of custom Claude skills that extend Claude's capabilities with specialized workflows for productivity, email management, calendar operations, and information retrieval. 

## Project Structure
- `/` - Root directory containing the core `README.md`.
- `/[skill-name]/` - Individual skill directories (e.g., `recent-emails`, `set-up-workday`, `new-presentation`).
- `/[skill-name]/skill.md` - The core definition and instructions for each specific skill.
- `/references/` - Documentation, schemas, and guides (e.g., `how-to-build-claude-skills.md`, `claude-connections`).
- `/Ideas/` - Sandbox directory for drafting new skill concepts before implementation.

## Skill Architecture
Each Claude Skill is defined by a `skill.md` file located in its respective folder. 

### Format Rules
Every `skill.md` file MUST follow this strict YAML frontmatter format:
```markdown
---
name: skill-name
description: Brief description of what the skill does
---

# Skill Title

[Detailed instructions and workflow]
```

### Best Practices for Skill Development
1. **Size Limit:** Keep `skill.md` under 500 lines.
2. **Progressive Disclosure:** Design instructions that reveal complexity only when needed by the workflow.
3. **Guardrails:** Explicitly document success criteria and constraints within the prompt.
4. **Reusability:** Reference existing micro-skills (like `list-emails` or `list-files`) for consistent output formatting instead of rebuilding tables from scratch.

## Deployment Workflow
To deploy a skill to Claude:
1. Navigate to the specific skill's subfolder (e.g., `cd "DEV/Claude Skills/daily-calendars"`).
2. Compress the entire subfolder into a `.zip` file (e.g., `daily-calendars.zip`).
3. Upload the resulting zip file to Claude's custom Skills console.

## Standard Formats
- **Emails:** Skills returning emails should utilize the `list-emails` micro-skill format (executive-style tables, numbered rows, Gmail deep links, 35-word summaries).
- **Files:** Skills returning Drive files should utilize the `list-files` micro-skill format (type categorization, modification dates, Drive deep links).
- **Dates:** Leverage `reverse-date` and `reverse-month` logic for standardizing timeframes (YYYY-MM-DD or YYYY-MM).

## Core API Dependencies
Depending on the skill, the following external integrations are utilized via Claude Connections:
- Gmail API
- News/Web Retrieval APIs

## Daily Plans & Inline Verification

When the user asks "what's the plan for today?" or similar, read the latest plan entry in the Plans journal (`Journals/YYYY-MM Plans.md`) and present a **summary table grouped by priority**. Each priority group should be a table with columns: `#`, `Task`, `Status`, `Effort`. Use status icons: 🆕 New, 🔄 In Progress, ✅ Done. Include totals at the bottom.

### Completion Evidence

When a task is completed, append **Output** and **Verification** fields directly to the task block within the Plans journal. There is no separate audit file — all verification is recorded inline:

```markdown
###### N.N ✅ [Task title]
- **Action:** What was done
- **Delegate:** Name
- **Effort:** ~N mins
- **Output:** Link to deliverable, summary of result, or confirmation
- **Verification:**
  - [x] Specific thing verified
  - [x] Another verification item
```

Rules:
- Every task's verification is recorded **within its own task block** — never in a separate file
- `Output` must include a concrete deliverable (link, summary, or confirmation)
- `Verification` items start with `- [x]` (checked) and describe specific, concrete outcomes — not vague summaries

### Plans Journal Formatting

When a task is completed, both the **task-level icon** and the **priority section heading** must be updated:
1. **Task icon**: Change `🆕` → `✅` for each completed item (e.g., `###### 2.1 ✅ Update recent-emails constraints`)
2. **Priority heading**: Append `✅ Done` to the heading once all items in a priority group are complete
3. **Status tracking table** (where present): Update `❌` rows to `✅ Done` for items completed during the session

## Core Commands

### Check Repo Sync Status

When the user says "Check Repo", perform the following procedure to ensure the Git repository is synchronized:

1. **Verify No Uncommitted Changes** — Check `git status` to ensure the working directory is clean.
2. **Fetch Remote Changes** — Run `git fetch` to retrieve the latest remote state without merging.
3. **Compare Local and Remote** — Check if the local branch is ahead, behind, or has diverged from the remote tracking branch (e.g., using `git status` after fetching).
4. **Report Status** — Provide the user with a concise summary. If synced, confirm it. If not, state exactly what needs to be committed, pushed, or pulled.

### Check Git Versions

When the user says "Git Versions" or asks for recent versions, perform the following procedure:

1. **Run Git Log** — Execute `git log --oneline -n 5` to fetch the last 5 commits in the repository.
2. **Present to User** — Display the list directly to the user as a bulleted list or code block.
