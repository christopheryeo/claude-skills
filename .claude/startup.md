# Morning Startup Process

## 1. Sync Check
```bash
git fetch && git status
```
Confirm the local branch is in sync with `origin/main`. If behind, pull first. If ahead, investigate and commit/push before proceeding.

## 2. Orient to Yesterday's Work
- Read the most recent `plans/YYYY-MM-DD-plans.md` to recall what was planned.
- Read the most recent `plans/YYYY-MM-DD Audit.md` to recall what was completed.
- Note any deferred items, uncommitted skill files, or open questions carried forward.

## 3. Create Today's Plan File and Audit Template
Create **both files together** — never one without the other.

**`plans/YYYY-MM-DD-plans.md`:**
- Use the most recent `plans/YYYY-MM-DD-plans.md` as the format reference (status legend, section structure, effort table).
- Carry forward any incomplete or deferred skill ideas from yesterday.
- Add new tasks (e.g., uploading specific skills to Claude, testing new skill prompts).
- Group by priority (P1 highest → P4 lowest) with estimated effort per task.

**`plans/YYYY-MM-DD Audit.md`:**
- Create as a shell with today's date header and a placeholder for each priority group.
- Structure mirrors the plans file — one `## Priority N: <Name>` section per group, ready to receive `## N.N` task entries as work is completed.
- Do not pre-populate task entries; those are written as tasks are done.

## 4. Begin Work in Priority Order
Work through tasks top-to-bottom by priority. After completing each priority group:
- Write audit entries to `plans/YYYY-MM-DD Audit.md` (one `## N.N` block per task, following the strict format in `CLAUDE.md`).
- Update task icons in `plans/YYYY-MM-DD-plans.md` (`🆕` → `✅`) and append `✅ Done` to the priority heading.
- Commit: `git add . && git commit -m "Complete Priority N <name>"`
- Push to remote: `git push`

## 5. End-of-Day Wrap-Up
- Run a final completion audit verifying all planned items are genuinely complete.
- Append the final audit report to `plans/YYYY-MM-DD Audit.md`.
- Ensure all newly built `skill.md` files are properly documented in the `README.md`.
- Final commit and push.
- Confirm `git status` is clean.

---

## Key Preferences (Summary)
- **Always run the Sync Check on startup** to ensure you aren't overwriting remote work.
- **Audit and plans files are always updated together** — never one without the other.
- **Commits per priority group**, not per individual task.
- **Audit entries use the `## N.N Task Name` checklist format** — no summary bullet lists (see `CLAUDE.md` for full spec).
