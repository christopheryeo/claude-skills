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
1. Navigate to the specific skill's subfolder (e.g., `cd "DEV/Claude Skills/search-calendar"`).
2. Compress the entire subfolder into a `.zip` file (e.g., `search-calendar.zip`).
3. Upload the resulting zip file to Claude's custom Skills console.

## Standard Formats
- **Emails:** Skills returning emails should utilize the `list-emails` micro-skill format (executive-style tables, numbered rows, Gmail deep links, 35-word summaries).
- **Files:** Skills returning Drive files should utilize the `list-files` micro-skill format (type categorization, modification dates, Drive deep links).
- **Dates:** Leverage `reverse-date` and `reverse-month` logic for standardizing timeframes (YYYY-MM-DD or YYYY-MM).

## Core API Dependencies
Depending on the skill, the following external integrations are utilized via Claude Connections:
- Gmail API
- News/Web Retrieval APIs

## Daily Plans & Auditing

When the user asks "what's the plan for today?" or similar, read the latest file in the `plans/` directory (by date in filename, e.g., `2026-02-25-plans.md`) and present a **summary table grouped by priority**. Each priority group should be a table with columns: `#`, `Task`, `Status`, `Effort`. Use status icons: 🆕 New, 🔄 In Progress, ✅ Done. Include totals at the bottom.

### Development Auditing

When an item in the plans file is executed during a development session, its results **must be audited** at the end of execution. The findings and verification checks must be written to the appropriate accompanying audit file (e.g., `plans/2026-02-25 Audit.md`) to capture a permanent trail of development progress. This ensures transparency and prevents plan status icons from diverging from the actual codebase state. Always update the audit file with specific pass/fail outcomes against the task's objectives.

### Audit File Formatting (`plans/YYYY-MM-DD Audit.md`)

Each completed task must be recorded as an individual block in the following exact format — **do not use summary bullet lists**:

```markdown
## [Task Number] [Task name]
**Status:** ✅ Done
**Files:** `path/to/file1.md`, `path/to/file2.md`
**Objective:** One sentence describing the goal of the task.
**Verification Checklist:**
- [x] Specific thing that was verified or done
- [x] Another specific verification item
```

Rules:
- Every task gets its **own `## N.N` heading** — never group multiple tasks under one heading
- `Status` is always `✅ Done` once executed
- `Files` lists the exact files modified (use backtick-quoted relative paths)
- `Objective` is a single clear sentence of what the task accomplished
- `Verification Checklist` items start with `- [x]` (checked) and describe specific, concrete outcomes — not vague summaries
- Tasks in the same priority group share a single `## Priority N: <Name>` parent header with no sub-introduction or summary section; individual `## N.N` blocks follow directly

### Plans File Formatting (`plans/YYYY-MM-DD-plans.md`)

When a task is completed, both the **task-level icon** and the **priority section heading** must be updated:
1. **Task icon**: Change `🆕` → `✅` for each completed item (e.g., `#### 2.1 ✅ Update recent-emails constraints`)
2. **Priority heading**: Append `✅ Done` to the heading once all items in a priority group are complete
3. **Status tracking table** (where present): Update `❌` rows to `✅ Done` for items completed during the session

Both the audit file and the plans file must be updated **together** at the end of each task.

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
