# Daily Files – Quick Reference Guide

## TL;DR

Replace four separate skills with one unified **daily-files** skill and four sub-commands:

```
daily-files topic [keyword]      ← Replaces topic-files
daily-files recent [timeframe]   ← Replaces recent-files
daily-files workday [date]       ← Replaces work-day-files
daily-files folder [path]        ← Replaces list-files
```

---

## Quick Lookup Table

| What You Want | Old Skill | New Command | Example |
|---|---|---|---|
| **Find files about a topic** | topic-files | `daily-files topic` | `daily-files topic "product launch"` |
| **See recently changed files** | recent-files | `daily-files recent` | `daily-files recent last 3 days` |
| **Get today's work files** | work-day-files | `daily-files workday` | `daily-files workday today` |
| **List a specific folder** | list-files | `daily-files folder` | `daily-files folder /My Drive/Projects` |

---

## Sub-Command Syntax

### Topic Search
```
daily-files topic [keyword] [options]

Examples:
- "Find files about AI safety"
- "Pull all decks on the Q4 roadmap from last 6 months"
- "Show me everything related to Acme Corp"
```

### Recent Files
```
daily-files recent [timeframe]

Examples:
- "Show me recent files" (defaults to last 24 hours)
- "What changed in the last 3 hours?"
- "Files modified this week"
```

### Work-Day Files
```
daily-files workday [date]

Examples:
- "Show me today's files"
- "What did I work on October 30?"
- "Files in my November 15 folder"
```

### Generic Folder Listing
```
daily-files folder [path] [options]

Examples:
- "List files in my Projects folder"
- "What's in the Shared drives/Marketing folder?"
```

---

## Migration Checklist

- [ ] Review consolidated SKILL.md
- [ ] Upload daily-files to Claude Skills
- [ ] Test all four sub-commands
- [ ] Update dependent skills (set-up-workday, etc.)
- [ ] Archive old skills

---

## File Locations

All files are in `/Claude Skills/` folder:

✅ `daily-files/SKILL.md` - Main skill definition (409 lines)
✅ `CONSOLIDATION-SUMMARY.md` - Full consolidation details
✅ `DAILY-FILES-QUICK-REFERENCE.md` - This quick reference
