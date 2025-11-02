# Claude Skills Library

**Version:** 1.13.0  
**Last Updated:** November 2, 2025  
**Maintained by:** Chris Yeo

A collection of custom Claude skills that extend Claude's capabilities with specialized workflows for productivity, email management, calendar operations, and information retrieval.

---

## Version History

### v1.13.0 (November 2, 2025)
- **New Skill Ideas**: Added documentation for `proposal-skill`, `evening-summary`, and `weekly-focus-planner`
- **Enhanced Documentation**: Updated customer brief specifications and added detailed use cases
- **Repository Structure**: Added new Ideas directory for future skill development

### v1.12.0 (November 2, 2025)
- **Enhanced Skill**: Updated `actioned-emails` with improved documentation and clearer instructions
- **New Skill**: Added `starred-email` for focused Gmail starred email management
- **Documentation**: Enhanced skill creation instructions with Codex-specific guidance
- **Templates**: Added comprehensive script templates with error handling

### v1.10.0 (November 1, 2025)
- **Documentation**: Enhanced skill creation instructions with cross-references
- **References**: Added claude-connections and claude-skills references
- **Templates**: Updated skill creation templates and best practices

### v1.9.0 (November 1, 2025)
- **Documentation**: Added comprehensive guide on building Claude skills
- **References**: Created detailed how-to guide for skill development

### v1.8.0 (November 1, 2025)
- **recent-emails**: Enhanced Gmail email retrieval with advanced filtering, newsletter detection, and comprehensive activity analysis

### v1.7.0 (October 31, 2025)
- **recent-files**: Enhanced Google Drive file discovery with activity insights and chronological work narrative

### v1.6.0 (October 31, 2025)
- **product-white-paper**: Added skill for generating enterprise-grade product white papers

### v1.5.0 (October 31, 2025)
- **presentation-jobs**: Added Steve Jobs-style presentation creation with 3-Second Rule methodology

### v1.4.0 (October 31, 2025)
- **presentation-outline**: Added skill to transform Google Docs into structured presentation outlines

### v1.3.0 (October 26, 2025)
- **work-day-files**: Added file listing and summarization for work-day folders

### v1.2.0 (October 25, 2025)
- **work-day**: Added Google Drive folder management for work documents with date-based structure
- **reverse-month**: Added month conversion and standardization (YYYY-MM format)

### v1.1.0 (October 23, 2025)
- **reverse-date**: Added date conversion and natural language date parsing

### v1.0.0 (October 21, 2025)
- Initial release with 5 core skills
- **recent-emails**: Gmail email retrieval functionality
- **search-calendar**: Google Calendar search with fuzzy matching
- **recent-drive**: Google Drive file discovery
- **news-snapshot**: International and Singapore news briefing
- **morning-recon-brief**: Comprehensive executive morning brief
- Established standardized folder structure with `skill.md` files
- Created documentation and usage guidelines

---

## What Are Claude Skills?

Claude Skills are structured prompt templates that teach Claude how to perform specific tasks consistently and effectively. Each skill is defined in YAML frontmatter format with a name, description, and detailed instructions.

### Key Components
- **SKILL.md**: Core definition and instructions
- **Scripts**: Executable code for the skill
- **References**: Documentation and schemas
- **Assets**: Templates and resources

### Getting Started
- [How to Build Claude Skills](./references/how-to-build-claude-skills.md)
- [Available Integrations](./references/claude-connections)
- [Existing Skills Reference](./references/claude-skills)

## Available Skills

### ⭐ **starred-email**
Focused Gmail assistant that lists and summarizes your starred emails with actionable insights. Retrieves actual Gmail data, prioritizes recent starred messages, and highlights action items with direct Gmail links. Includes filtering by timeframe, keywords, and participants.

### 🔄 **actioned-emails**
Unified Gmail recap that combines recently sent emails with starred follow-ups. Blends recently sent and starred Gmail emails into a single executive recap with summaries, metadata, and follow-up prompts. Use when users ask to review "what I sent" or "what I followed up on" recently, combine sent mail and starred mail into one recap, surface pending actions from starred threads alongside recent outbound communication, or provide a short executive summary of recent activity plus what still needs attention.

### 📧 **recent-emails**
Advanced Gmail email retrieval with support for received, sent, drafted, and starred emails. Features include newsletter filtering, chronological work narrative, and comprehensive activity analysis. Returns emails with timestamps, senders/recipients, subject lines, summaries, and direct Gmail links.

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

### 📝 **presentation-outline**
Transforms Google Docs into structured presentation outlines with titles, subtitles, and bullet points. Generates up to 10 slides with clear organization and logical flow, ideal for quickly creating presentation drafts from existing documentation.

### 🎯 **presentation-jobs**
Create powerful presentations using Steve Jobs's 3-Second Rule methodology. Applies the Billboard Test principles for minimal cognitive load, maximum visual impact, and elegant slide design. Ideal for product launches, pitches, and keynotes that require high audience retention and visual clarity.

### 📄 **product-white-paper**
Generate comprehensive Enterprise AI Product White Papers using existing documentation as source material. Creates authoritative, research-backed documents that educate buyers and present solutions to complex business problems, with a focus on strategic value and ROI for enterprise audiences.

### 🔍 **recent-files**
Track and analyze recent Google Drive activity with detailed metadata and insights. Features include chronological work narratives, activity patterns, project focus areas, and client-specific tracking. Ideal for reviewing work history, tracking project progress, and maintaining awareness of team activities.

## Folder Structure

```
/
├── recent-emails/          # Gmail email retrieval skill
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
├── presentation-outline/  # Presentation outline generation
│   ├── guidelines/        # Presentation guidelines
│   └── skill.md          # Skill implementation
├── presentation-jobs/     # Steve Jobs-style presentations
│   └── skill.md          # Skill implementation
├── product-white-paper/   # Enterprise white paper generation
│   ├── references/       # White paper templates and guidelines
│   └── skill.md          # Skill implementation
├── recent-files/         # Drive activity tracking and insights
│   └── skill.md          # Skill implementation
└── README.md             # This file
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

## Reference Materials

### Core Documentation
- [How to Build Claude Skills](./references/how-to-build-claude-skills.md) - Comprehensive guide to creating custom Claude skills
- [Claude Connections](./references/claude-connections) - Available integrations and their capabilities
- [Claude Skills Reference](./references/claude-skills) - Catalog of existing skills and patterns

### Development Resources
- [Skill Creation Instructions](./references/instructions.md) - Step-by-step guide for AI-assisted skill development
- [Skill Templates](./templates/) - Starter templates for common skill types
- [Codex Integration Guide](./references/instructions.md#step-10-implementation-workflow-for-codex) - Optimizing skills for OpenAI Codex

### Best Practices
- Keep SKILL.md under 500 lines
- Use progressive disclosure
- Document success criteria and guard rails
- Reference existing skills to avoid duplication

## Development Workflow

1. **Plan**
   - Review existing skills and connections
   - Define success criteria and guard rails
   - Design with progressive disclosure in mind

2. **Develop**
   - Create SKILL.md with clear instructions
   - Implement required scripts and assets
   - Document all components

3. **Test**
   - Verify skill identification with different phrasings
   - Test edge cases and error conditions
   - Validate integration points

4. **Deploy**
   - Package the skill
   - Document usage examples
   - Add to the skills catalog

## Requirements

### API Integrations
- Gmail API for email-related skills
- Google Calendar API for calendar operations
- Google Drive API for file management
- News APIs for news retrieval (optional)
- See [claude-connections](./references/claude-connections) for full list

### Development Environment
- Python 3.8+
- Git for version control
- Text editor or IDE
- Access to required APIs and services

See individual skill folders for specific setup instructions.
