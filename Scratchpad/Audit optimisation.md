# Audit Optimisation — Collapsing Audit Files into the Plans Journal

## Context: Original Prompt

> **Question:** The audit file — is it really needed, or can the plans file carry its own verification?

## Strategic Consideration

Short answer: yes, but not in its current form.

The audit file does three things the plans file can't do on its own:

### What's genuinely valuable

The verification checklist is the real differentiator. When Mary's audit confirms she updated Lead Gen Log #37, referenced both engagement models, and threaded the Gmail draft correctly — that's quality assurance you can't derive after the fact. Without it, you're trusting the task was done right purely on faith. For a CEO managing six autonomous AI workers, that's the difference between delegation and abdication.

### What's not pulling its weight

The status field, action narrative, and output links are largely redundant. If a task is in the audit file at all, it's done — so "Status: ✅ Done" adds nothing. The action narrative repeats what the output artifact already shows. And the output link is useful, but could live in the plans file itself as a one-liner upon completion.

### The real question is architectural

You have 49 files in Mary's Plans folder alone. That's roughly half audit files — a parallel paper trail that duplicates effort. The overhead compounds across six team members.

## Recommendation

Collapse the audit into the plans file. When a task completes, append two things directly to the plans entry: the output link and the verification checklist (pass/fail). Kill the standalone audit file entirely. You keep the accountability value — which is real — without the file proliferation and narrative redundancy.

That gives you one file per day per team member instead of two, the verification gates stay intact, and everything is traceable in a single document.

## What Must Change in the `daily-plans` Skill

The completed task block becomes:

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

### Changes by section in `daily-plans/SKILL.md`:

1. **Header/intro (line 9)** — Remove "Audit files remain in a separate `Plans/` folder." Replace with: "Completion evidence (output links and verification checklists) is recorded inline within each task block."

2. **Dependency table (lines 17–26)** — The LOG row references "write an audit entry" — change to "append Output and Verification fields to the task block."

3. **Locating Files (lines 34–38)** — Remove step 3 entirely (the `Plans/` folder for audit files). The `Plans/` folder is no longer needed by this skill.

4. **File Locations and Naming (lines 56–58)** — Delete the audit file line (`Plans/YYYY-MM-DD Audit.md`). Only the Plans journal remains.

5. **CREATE operation (lines 98, 159–165)** — Remove "plus a shell audit file in `Plans/`" from the purpose statement. Delete step 6 entirely (audit shell creation). Renumber step 7 → 6.

6. **EXECUTE operation, step 6 (lines 238–248)** — Replace "Write the audit entry" with: "Append completion evidence to the task block." Re-open the Plans journal, locate the task heading just updated to ✅, and append `**Output:**` and `**Verification:**` fields below the existing Action/Delegate/Effort lines. No separate file write.

7. **LOG operation, step 4 (lines 287–298)** — Same treatment. Replace the audit file write with inline append. Since LOG already writes the task as ✅ via NEW, the Output and Verification fields are included in the initial task block rather than written to a separate file.

8. **LOG step 5 (line 299)** — Update confirmation text: remove "and the audit file" — it now just confirms the task was logged in the Plans journal with verification.

9. **Edge case (line 421)** — "Deleting a completed task: Allow it but warn that the audit entry will remain (audit entries are never deleted)" — replace with: "Allow it but confirm first, as the verification record will also be removed."

10. **The `Plans/` folder itself** — If audit files were the only reason `Plans/` existed, remove the folder reference from the skill entirely.

### Also needs updating (outside the skill):

- **Root `CLAUDE.md`** — "Daily Plans & Auditing" and "Audit File Formatting" sections define the standalone audit format. These must be rewritten to describe inline verification within the plans journal.
- **`.claude/CLAUDE.md`** — Same audit formatting rules duplicated here.
