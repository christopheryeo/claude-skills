# Claude Skills Library

**Version:** 1.3.0  
**Last Updated:** October 26, 2025  
**Maintained by:** Chris Yeo

A collection of custom Claude skills that extend Claude's capabilities with specialized workflows for productivity, email management, calendar operations, and information retrieval.

---

## Version History

### v1.3.0 (October 26, 2025)
- **work-day-files**: Added file listing and summarization for work-day folders

### v1.2.0 (October 25, 2025)
- **work-day**: Added Google Drive folder management for work documents with date-based structure
- **reverse-month**: Added month conversion and standardization (YYYY-MM format)

### v1.1.0 (October 23, 2025)
- **reverse-date**: Added date conversion and natural language date parsing

### v1.0.0 (October 21, 2025)
- Initial release with 5 core skills
- **emails-recent**: Gmail email retrieval functionality
- **search-calendar**: Google Calendar search with fuzzy matching
- **recent-drive**: Google Drive file discovery
- **news-snapshot**: International and Singapore news briefing
- **morning-recon-brief**: Comprehensive executive morning brief
- Established standardized folder structure with `skill.md` files
- Created documentation and usage guidelines

---

## What Are Claude Skills?

Claude Skills are structured prompt templates that teach Claude how to perform specific tasks consistently and effectively. Each skill is defined in YAML frontmatter format with a name, description, and detailed instructions.

## Available Skills

### 📧 **emails-recent**
Lists the most recent emails received, sent, or drafted in Gmail. Defaults to last 24 hours, or accepts custom timeframe. Returns emails with timestamps, senders/recipients, subject lines, summaries, and clickable links sorted by recency.

### 📅 **search-calendar**
Search your Google Calendar across multiple dimensions - by day, date, week, subject, attendee names, and emails. Supports flexible natural language queries with fuzzy matching for intelligent results.

### 📂 **recent-drive**
Lists the most recent files created or modified in Google Drive. Defaults to last 24 hours, or accepts custom timeframe. Returns files with modification dates, summaries, and clickable links sorted by recency.

### 📰 **news-snapshot**
Retrieve and summarize current international and Singapore news stories with headlines, brief context, and source links in a professional executive format. Use when you need a quick daily news briefing with verified sources.

### 🌅 **morning-recon-brief**
Executive morning intelligence brief that combines unread emails, today's calendar, Drive updates, tasks, and news into a comprehensive decision-ready report. Triggered by "Run my Morning Brief".

### 📆 **reverse-date**
Converts between natural language date descriptions and standard date formats. Supports relative dates (e.g., "two days ago"), date formatting, and date difference calculations.

### 📅 **reverse-month**
Converts dates to standardized YYYY-MM format, extracting just the year and month components. Ideal for monthly reporting, aggregations, and calendar operations.

### 🗂️ **work-day**
Manages Google Drive folder structure for work documents, automatically creating month (YYYY-MM Work) and day (YYYY-MM-DD) folders. Ensures consistent organization for daily work files.

### 📄 **work-day-files**
Lists and summarizes files in work-day folders with 40-word summaries. Navigates the YYYY-MM Work/YYYY-MM-DD folder structure to retrieve and summarize documents, spreadsheets, and other files for a given work day.

## Folder Structure

```
/
├── emails-recent/          # Gmail email retrieval skill
│   └── skill.md           # Skill implementation
├── search-calendar/        # Google Calendar search skill
│   └── skill.md           # Skill implementation
├── recent-drive/           # Google Drive file discovery skill
│   └── skill.md           # Skill implementation
├── news-snapshot/          # News briefing skill
│   └── skill.md           # Skill implementation
├── morning-recon-brief/    # Comprehensive morning brief skill
│   └── skill.md           # Skill implementation
├── reverse-date/          # Date conversion and parsing skill
│   ├── scripts/           # Python scripts for date handling
│   │   └── convert_date.py
│   └── skill.md           # Skill implementation
├── reverse-month/         # Month conversion and parsing skill
│   ├── scripts/           # Python scripts for month handling
│   │   └── convert_month.py
│   └── skill.md           # Skill implementation
├── work-day/              # Work day folder management skill
│   └── skill.md           # Skill implementation
├── work-day-files/        # Work day file listing and summarization
│   └── skill.md           # Skill implementation
└── README.md               # This file
```

Each subfolder contains a `skill.md` file that implements the Claude skill with its complete instructions and workflow.

## How to Use

1. **Prepare the skill**: Navigate to the skill's subfolder you want to use
2. **Create a zip file**: Compress the entire subfolder into a `.zip` file (e.g., `search-calendar.zip`)
3. **Upload to Claude**: Upload the zip file to Claude's Skills functionality
4. **Invoke the skill**: Reference the skill by name or use the trigger phrase specified in the skill description
5. **Customize**: Edit the `skill.md` files to match your specific needs and preferences before zipping

## Skill File Format

Each skill follows this YAML frontmatter format:

```markdown
---
name: skill-name
description: Brief description of what the skill does
---

# Skill Title

[Detailed instructions and workflow]
```

## Requirements

Some skills require integration with external services:
- Gmail API access for email-related skills
- Google Calendar API for calendar operations
- Google Drive API for file management
- News APIs for news retrieval (optional)

See individual skill folders for specific setup instructions.
