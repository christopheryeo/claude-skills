---
name: daily-journals
description: Manages markdown journal files in a Journals/ folder — creating new journal files, adding date-stamped entries, and deleting entries. A journal is a markdown file named with reverse-month and purpose (e.g., "2026-03 Activities.md") containing chronological entries grouped under reverse-date headers. Use whenever the user says "create a journal", "new journal", "journal entry", "add to journal", "delete journal entry", "remove entry", "show journals", or mentions logging thoughts, activities, notes, or reflections into a dated journal format.
---

# Daily Journals

A skill for managing structured markdown journal files. Journals live in a `Journals/` folder resolved from the user's selected workspace and contain chronological entries grouped by date.

---

## What Is a Journal?

A journal is a **markdown file** that collects entries over time, grouped under date headers.

- **Filename format:** `YYYY-MM <Purpose>.md` — the reverse-month prefix keeps files sorted chronologically and the purpose label describes the journal's theme.
  - Examples: `2026-03 Activities.md`, `2026-03 Ideas.md`, `2026-04 Meeting Notes.md`
- **Date headers:** Each group of entries sits under a heading using reverse-date format (`YYYY-MM-DD`), which represents the date those entries were recorded.
- **Entries:** Free-form markdown content beneath each date header — bullet points, paragraphs, checklists, or any markdown the user wants.

### Journal File Structure

```markdown
# 2026-03 Activities

## 2026-03-03

- Had a productive morning session working on the Claude Skills library
- Reviewed the daily-plans skill and identified improvements

## 2026-03-02

- Drafted the customer brief for BeeNext
- Sent follow-up emails to three prospects
```

Key principles:
- **Newest entries first.** The most recent date header appears at the top of the file (reverse chronological order), so opening the journal always shows the latest entries.
- **One file per month per purpose.** A journal file covers a single calendar month. When a new month begins, a new file is created.
- **The month in the filename must match the entries.** A file named `2026-03 Activities.md` only contains entries with `2026-03-xx` date headers.

---

## Locating the Journals/ Folder

This skill is folder-agnostic — it works from whatever folder the user has selected (mounted).

1. **Determine the mounted root.** The user's selected workspace is the mount point.
2. **Look for `Journals/` at that root.** Check if a `Journals/` directory already exists at the top level of the mounted folder.
3. **Create it if missing.** If no `Journals/` folder exists, create one at the mounted root.

All file operations use this resolved path.

---

## Detecting the Sub-Command

| Trigger phrases | Operation |
|---|---|
| "create a journal", "new journal", "start a journal for [purpose]" | **create-journal** |
| "add journal entry", "journal entry", "log to journal", "add to [purpose] journal" | **create-entry** |
| "delete journal entry", "remove entry from journal" | **delete-entry** |
| "consolidate entries", "consolidate [folder]", "consolidate entries for [folder]" | **consolidate-entries** |

If the intent is ambiguous, ask which operation is intended.

---

## Operation: CREATE-JOURNAL

**Purpose:** Create a new, empty journal file for a given month and purpose.

### Steps

1. **Determine the month.** Default to the current month (using reverse-month format `YYYY-MM`). If the user specifies a different month, convert it using reverse-month logic.

2. **Determine the purpose.** The user must provide a purpose label — this is the descriptive part of the filename (e.g., "Activities", "Ideas", "Meeting Notes", "Reflections"). If not provided, ask: "What would you like to call this journal? For example: Activities, Ideas, Meeting Notes."

3. **Check for duplicates.** Look in the Journals/ folder for an existing file matching `YYYY-MM <Purpose>.md`. If one exists, inform the user and ask whether they want to open/use the existing one or create a new journal with a different name.

4. **Create the file** using this template:

```markdown
# YYYY-MM <Purpose>

```

The file starts with just the title heading — entries will be added later via the create-entry sub-command. The title mirrors the filename for consistency.

5. **Confirm creation.** Tell the user the journal has been created, show the filename and path, and mention they can start adding entries.

### Examples

**User says:** "Create a journal for Activities"
**Result:** `Journals/2026-03 Activities.md`

**User says:** "Start a new Ideas journal for April"
**Result:** `Journals/2026-04 Ideas.md`

**User says:** "New journal called Meeting Notes"
**Result:** `Journals/2026-03 Meeting Notes.md`

---

## Operation: CREATE-ENTRY

**Purpose:** Add one or more entries to an existing journal file under the appropriate date header.

### Steps

1. **Determine the target journal.** The user may specify a journal by purpose name (e.g., "add to Activities journal") or by filename. If only one journal exists for the current month, use it. If multiple journals exist and the user hasn't specified which, list them and ask.

2. **Determine the date.** Default to today's date in reverse-date format (`YYYY-MM-DD`). If the user specifies a different date, convert it accordingly. The date must fall within the journal file's month — if it doesn't, either find the correct month's journal or offer to create one.

3. **Read the journal file.** Load the current contents to determine where to insert the new entry.

4. **Find or create the date header.** Scan the file for an existing `## YYYY-MM-DD` header matching the target date.
   - **If the header exists:** Insert the new entries below the last existing entry under that header (before the next date header or end of file).
   - **If the header does not exist:** Create a new `## YYYY-MM-DD` header and insert it in the correct position to maintain reverse chronological order (newest first). The new header goes:
     - At the top (just after the `# Title` heading) if the date is more recent than all existing headers.
     - Between two existing headers if the date falls between them.
     - At the bottom if the date is older than all existing headers.

5. **Write the entries.** Add the user's content beneath the date header. Entries are free-form markdown — respect whatever format the user provides (bullet points, paragraphs, checklists, etc.). If the user provides plain text without formatting, default to bullet points prefixed with `- `.

6. **Save the file** and confirm what was added, showing the date header and a brief preview of the entry.

### Handling Multiple Entries

If the user provides several items in one go (e.g., a list of things they did), add them all under the same date header as separate bullet points or in whatever structure the user provided.

### Auto-Creating the Journal

If no journal file exists for the target month and purpose, offer to create one first using the CREATE-JOURNAL operation, then proceed with the entry. Don't silently create journals — the user should confirm the purpose name.

### Examples

**User says:** "Add to Activities journal: Had a productive morning session on Claude Skills"
**Result:** Opens `2026-03 Activities.md`, finds or creates `## 2026-03-03`, adds:
```markdown
## 2026-03-03

- Had a productive morning session on Claude Skills
```

**User says:** "Journal entry for Ideas: Consider adding a search sub-command to daily-journals"
**Result:** Opens `2026-03 Ideas.md`, finds or creates `## 2026-03-03`, adds the entry.

**User says:** "Log these to the Meeting Notes journal for yesterday: Met with BeeNext team, discussed Q2 roadmap, agreed on follow-up actions"
**Result:** Opens `2026-03 Meeting Notes.md`, finds or creates `## 2026-03-02`, adds:
```markdown
## 2026-03-02

- Met with BeeNext team
- Discussed Q2 roadmap
- Agreed on follow-up actions
```

---

## Operation: DELETE-ENTRY

**Purpose:** Remove one or more entries from a journal file, with confirmation before any destructive action.

### Steps

1. **Determine the target journal.** Same resolution logic as CREATE-ENTRY — the user may specify by purpose name, filename, or if only one journal exists for the relevant month, use it automatically. If ambiguous, list available journals and ask.

2. **Determine the target date.** The user must indicate which date's entries to delete — either explicitly (e.g., "delete entries from 2026-03-02") or implicitly ("delete yesterday's entries"). Default to today only if the user says something like "delete today's entry". Convert to reverse-date format (`YYYY-MM-DD`).

3. **Read the journal file.** Load the current contents to locate the target entries.

4. **Identify the entries to delete.** Find the `## YYYY-MM-DD` header matching the target date.
   - **If the header does not exist:** Inform the user that no entries were found for that date — nothing to delete.
   - **If the header exists:** Identify all content beneath it (up to the next `## YYYY-MM-DD` header or end of file). This is the deletion scope.

5. **Narrow the scope (optional).** If the user wants to delete only specific entries rather than all entries under a date, match by content. Show numbered entries under the date header and ask which to remove. If the user said "delete all entries for [date]", skip this step and target everything under the header.

6. **Show confirmation.** Before deleting, display exactly what will be removed — the date header and the entries beneath it (or the specific entries if narrowed). Ask: "Are you sure you want to delete these entries? This cannot be undone."
   - **If confirmed:** Proceed to step 7.
   - **If declined:** Abort and confirm no changes were made.

7. **Remove the entries.** Delete the identified content from the file.
   - **If deleting all entries under a date:** Remove the `## YYYY-MM-DD` header and all content beneath it up to the next header or end of file.
   - **If deleting specific entries:** Remove only those lines, leaving the date header and other entries intact.
   - **If the date header has no remaining entries after partial deletion:** Remove the now-empty date header as well.

8. **Save the file** and confirm what was deleted, including the date and a brief description of the removed content.

### Archival Consideration

Deleted entries are **not archived** by default — deletion is permanent. If the user expresses concern about losing content, suggest one of these alternatives before proceeding:
- **Copy first:** Offer to show the entries so the user can copy them before deletion.
- **Move instead of delete:** Offer to move entries to a different date header or journal rather than removing them entirely.

The skill does not maintain a trash or history log. If archival is important, the user should keep a separate backup journal or use version control on the Journals/ folder.

### Examples

**User says:** "Delete today's entries from the Activities journal"
**Result:** Opens `2026-03 Activities.md`, finds `## 2026-03-03`, shows entries, asks for confirmation, then removes the header and all entries beneath it.

**User says:** "Remove the entry about BeeNext from yesterday's Meeting Notes journal"
**Result:** Opens `2026-03 Meeting Notes.md`, finds `## 2026-03-02`, lists numbered entries, user selects the BeeNext entry, confirms, and only that entry is removed.

**User says:** "Delete all entries for 1 March from Ideas"
**Result:** Opens `2026-03 Ideas.md`, finds `## 2026-03-01`, shows all entries under that date, asks for confirmation, then removes the header and all entries.

---

## Operation: CONSOLIDATE-ENTRIES

**Purpose:** Scan all reverse-date files in a named sub-folder and consolidate their contents into journal files, grouped by month.

### Steps

1. **Determine the target sub-folder.** The user provides a folder name (e.g., "plans", "scratchpad"). Resolve it relative to the mounted root. If the folder does not exist, inform the user and stop — do not proceed.

2. **List and sort all reverse-date files.** Scan the sub-folder for files whose names begin with a `YYYY-MM-DD` prefix (e.g., `2026-03-15-plans.md`). Ignore any files that do not match this pattern. Sort all matching files from oldest to newest by their date prefix.

3. **Group files by month.** Partition the sorted file list into month buckets (`YYYY-MM`). Each bucket will map to its own journal file (e.g., files dated `2026-03-xx` → `Journals/2026-03 <FolderName>.md`).

4. **Derive the journal purpose label.** Use a title-cased version of the sub-folder name as the purpose (e.g., `plans` → `Plans`, `scratchpad` → `Scratchpad`).

5. **For each month bucket (oldest month first):**

   a. **Locate or create the journal file.** Check `Journals/` for a file named `YYYY-MM <Purpose>.md`. If it does not exist, create it using the CREATE-JOURNAL logic (file with just the `# YYYY-MM <Purpose>` title heading). Do not ask for confirmation — purpose and month are already known.

   b. **For each file in the bucket (oldest date first):**
      - Extract the date from the filename prefix (`YYYY-MM-DD`).
      - Read the journal file and check whether a `## YYYY-MM-DD` header for that date already exists.
      - **If the header already exists:** Skip this file silently — it has already been consolidated.
      - **If the header does not exist:** Read the raw contents of the source file in full and add them as a new entry under a `## YYYY-MM-DD` header, using the CREATE-ENTRY insertion logic to maintain reverse-chronological order.

6. **Report the outcome.** After processing all files, provide a concise summary to the user:
   - How many files were processed
   - How many entries were written vs. skipped (already existed)
   - Which journal files were created or updated (with filenames)

### Raw Content Handling

The full raw contents of each source file are written as-is into the journal entry — no summarisation, trimming, or reformatting. The content sits directly beneath the `## YYYY-MM-DD` date header exactly as it appears in the source file.

### Cross-Month Behaviour

Files spanning multiple months are each written into the journal file for their own month. There is no upper limit on how many months can be consolidated in a single run — all files found in the sub-folder are processed.

### Duplicate Protection

A file is skipped if and only if a `## YYYY-MM-DD` header with the exact same date already exists in the target journal. This check is date-based — it does not compare content — so if an entry was manually written for that date, the source file is still skipped to avoid duplication.

### Examples

**User says:** "Consolidate entries for plans"
**Sub-folder:** `Plans/` containing `2026-02-28-plans.md`, `2026-03-01-plans.md`, `2026-03-14-plans.md`
**Result:**
- Creates or opens `Journals/2026-02 Plans.md` → writes entry for `2026-02-28`
- Creates or opens `Journals/2026-03 Plans.md` → writes entries for `2026-03-01` and `2026-03-14`
- Reports: "3 files processed, 3 entries written across 2 journal files."

**User says:** "Consolidate entries for scratchpad"
**Sub-folder:** `Scratchpad/` containing `2026-03-10-scratchpad.md` (already in journal), `2026-03-12-scratchpad.md` (new)
**Result:**
- Opens `Journals/2026-03 Scratchpad.md` → skips `2026-03-10` (already exists), writes `2026-03-12`
- Reports: "2 files processed, 1 entry written, 1 skipped (already consolidated)."

---

## Edge Cases

- **No Journals/ folder exists:** Create it automatically before proceeding.
- **User doesn't specify a purpose:** Ask for one — don't default to a generic name.
- **Duplicate filename:** Warn and ask whether to use the existing file or pick a new name.
- **Month mismatch:** If the user asks to create a "March journal" but it's April, use March (`2026-03`) as requested — don't force the current month.
- **Purpose with special characters:** Sanitise the purpose label for safe filenames — replace characters like `/`, `\`, `:` with hyphens.
- **Entry date outside the journal's month:** Don't add a March entry to an April journal. Find or offer to create the correct month's file.
- **Adding to an empty journal:** The file may only contain the `# Title` heading — insert the date header directly after it.
- **Multiple entries for the same date:** Append below existing entries under that date header, don't create a duplicate header.
- **User doesn't specify a journal and multiple exist:** List available journals for the current month and ask which one.
- **Deleting from a date with only one entry:** After removing the entry, also remove the now-empty date header.
- **No entries found for the specified date:** Inform the user — don't silently do nothing. List available dates in the journal so they can pick the right one.
- **User asks to delete an entire journal file:** This skill only deletes entries within journals, not journal files themselves. Clarify the distinction and suggest the user delete the file manually if that's the intent.
- **Ambiguous entry match:** If the user describes an entry to delete but it matches multiple entries, list them numbered and ask which one(s) to remove.
- **consolidate-entries — sub-folder has no reverse-date files:** Inform the user that no files matching the `YYYY-MM-DD` naming pattern were found in that folder — nothing to consolidate.
- **consolidate-entries — sub-folder not found:** Inform the user the folder doesn't exist at the mounted root and stop. Do not create the folder.
