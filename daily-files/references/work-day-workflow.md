# Work-Day Workflow

Use this workflow to ensure the SNMG18 Working Docs month/day folder structure exists for a target date.

## Target Structure

```text
SNMG00 Management/
`-- SNMG18 Working Docs/
    `-- YYYY-MM Work/
        `-- YYYY-MM-DD/
```

## Steps

1. Determine the target date.
   - If the user provides a date such as "tomorrow", "March 15", or `2026-03-20`, resolve it using the host-provided current date and timezone.
   - If no date is specified, use today's date in `Asia/Singapore`.
   - Convert to month format `YYYY-MM Work` and day format `YYYY-MM-DD`.
2. Verify parent folders.
   - Search Drive for `SNMG00 Management` with folder MIME type and `trashed = false`.
   - Search for `SNMG18 Working Docs` inside `SNMG00 Management` using the parent filter.
   - If either parent is missing or ambiguous, stop and report that the parent folders must be resolved first.
3. Check or create the month folder.
   - Search for `{YYYY-MM Work}` inside `SNMG18 Working Docs`.
   - If found, record status `Exists`.
   - If missing, use the native Drive create-folder operation to create `{YYYY-MM Work}` under `SNMG18 Working Docs`, then record status `Created`.
4. Check or create the day folder.
   - Search for `{YYYY-MM-DD}` inside the month folder.
   - If found, record status `Exists`.
   - If missing, use the native Drive create-folder operation to create `{YYYY-MM-DD}` under the month folder, then record status `Created`.
5. Render using the work-day template in `output-format.md`.

## Confirmation Rules

- Do not ask for confirmation before creating the month/day folders when the target parent hierarchy is uniquely verified and the user's request is clearly to prepare work-day folders.
- Ask for confirmation if multiple parent folders match or if the date is ambiguous.
- Never create `SNMG00 Management` or `SNMG18 Working Docs`; those parent folders must already exist.

## Stop Conditions

- Stop if parent folders are missing, ambiguous, or inaccessible.
- Stop if the native Drive create-folder capability is unavailable.
- Do not use a non-native folder creation fallback without Christopher's explicit approval in an interactive session.
