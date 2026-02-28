# Claude Skills Library

**Version:** 1.36.1
**Last Updated:** December 15, 2025
**Maintained by:** Chris Yeo

A collection of custom Claude skills that extend Claude's capabilities with specialized workflows for productivity, email management, calendar operations, and information retrieval.

---

## Version History

### v1.37.0 (February 28, 2026)
- **Consolidated Email Skills**: Added `daily-emails` skill, uniting 7 sub-commands (recent, starred, actioned, topic, stakeholders, draft, format)
- **Repository Cleanup**: Removed 5 deprecated email skills (`recent-emails`, `starred-email`, `monitor-stakeholders`, `draft-email`, `list-emails`)

### v1.36.1 (December 15, 2025)
- **Skill Status Update**: Documented which skills are not yet loaded into Claude
  - Marked `actioned-emails` as pending Claude upload
  - Confirmed `new-presentation` is now available in Claude
  - Restated pending status for other skills still awaiting upload

### v1.36.0 (December 14, 2025)
- **New Skill Added**: `change-headings`
  - Converts document headings to normal paragraphs while preserving visual formatting
  - Maintains font size, weight, color, and inline styles
  - Useful for normalizing document structure without changing appearance

### v1.35.5 (November 12, 2025)
- **Enhanced Integration**: Updated `work-day-files` skill to integrate with `list-files` micro-skill
  - Standardized file presentation using the `list-files` table format
  - Improved metadata handling and summary generation
  - Enhanced documentation for consistent output with other file-related skills
- **Improved Formatting**: Updated `actioned-emails` to use `list-emails` for consistent email presentation
  - Unified email display format across all email-related skills
  - Improved status indicators and action item tracking
  - Enhanced documentation for better usability

### v1.35.4 (November 12, 2025)
- **Enhanced Formatting**: Updated `list-files` skill with improved table presentation
  - Streamlined table columns for better readability
  - Added Last Modified sorting by default (newest first)
  - Integrated folder context directly into file summaries
  - Simplified URL handling with embedded links in filenames
  - Enhanced documentation for consistent usage across skills

### v1.35.3 (November 12, 2025)
- **Enhanced Integration**: Updated `topic-files` skill to integrate with `list-files` micro-skill
  - Streamlined file presentation using the standardized `list-files` table format
  - Improved query construction and result handling
  - Enhanced documentation for search operators and filtering
  - Added support for activity-based file discovery

### v1.35.2 (November 12, 2025)
- **Enhanced Integration**: Updated `recent-files` skill to integrate with `list-files` micro-skill
  - Unified file presentation layer using `list-files` for consistent formatting
  - Improved metadata handling and summary generation
  - Added support for custom timeframes and file type filtering
  - Enhanced documentation for query construction and time formats

### v1.35.1 (November 12, 2025)
- **Enhanced Performance**: Optimized `recent-emails` skill for better token efficiency
  - Implemented strategic Gmail tool usage to minimize token consumption
  - Added selective message fetching with `read_gmail_message` for basic details
  - Reserved `read_gmail_thread` for unread, starred, or priority emails only
  - Improved documentation for query construction and time formats

### v1.35.0 (November 11, 2025)
- **Enhanced Integration**: Updated `recent-emails` and `starred-email` skills to integrate with `list-emails`
  - Unified email presentation layer using `list-emails` for consistent formatting
  - Added support for folder-specific Gmail deep links (Inbox/Sent/Drafts/Starred)
  - Enhanced email status indicators and star tracking
  - Improved action items and priority assessment sections

### v1.34.0 (November 10, 2025)
- **New Skill**: Added `list-emails` formatting micro-skill for consistent email tables
  - Standardizes numbered listings, summaries, and Gmail links for reuse across workflows
  - Provides optional sections for starred, priority, financial, and action item callouts
  - Designed to be embedded by retrieval-focused skills (e.g., `recent-emails`, `set-up-workday`)
  - Supports timezone-aware date formatting and multiple status indicators

### v1.33.1 (November 9, 2025)
- **New Skill**: Added `topic-files` for managing and summarizing document collections
  - Supports Google Drive query operations for targeted file retrieval
  - Includes comprehensive documentation for query operators
  - Features a structured summary checklist for consistent output

### v1.33.0 (November 8, 2025)
- **New Skill**: Added `topic-emails` for retrieving Gmail threads tied to a specific subject
  - Captures topic keywords, timeframe filters, and label exclusions before querying
  - Summarizes spotlight threads plus a complete topic log with Gmail deep links
  - Provides export guidance for creating follow-up CSVs manually
- **Repository Cleanup**: 
  - Removed `Ideas/topic-emails.md` now that the skill is implemented
  - Renamed `presentation-jobs` to `new-presentation` for consistency
  - Renamed `product-white-paper` to `new-product` for better clarity
- **Documentation Updates**:
  - Enhanced README with new folder structure
  - Updated skill references to reflect new naming conventions


### v1.31.1 (November 7, 2025)
- **Enhanced Skill**: Updated `presentation-jobs` with mandatory Sentient branding
  - Enforced Sentient Brand Guidelines for all presentations
  - Updated documentation to reflect consistent branding requirements
  - Improved integration with Sentient branding standards

### v1.31.0 (November 7, 2025)
- **Documentation Update**: Added details about sentient-pptx removal
  - Updated README to reflect project structure changes
  - Consolidated version history entries

### v1.30.0 (November 7, 2025)
- **Removed Skill**: Removed `sentient-pptx` directory and functionality
  - Consolidated presentation capabilities into `new-presentation`
  - Streamlined the project structure by removing redundant components
- **Enhanced Skill**: Further refined `new-proposal` workflow
  - Updated input requirements for executive-focused proposals
  - Moved SmartChat Analytics documentation to products folder
  - Streamlined proposal generation process
  - Improved Workday integration for document management

### v1.29.0 (November 6, 2025)
- **Enhanced Skill**: Updated `new-proposal` with streamlined workflow
  - Simplified input requirements for executive-focused proposals
  - Standardized on Google Docs output format
  - Added comprehensive case studies for SmartChat Analytics
  - Integrated with Workday for automatic document storage

### v1.28.0 (November 6, 2025)
- **New Asset**: Added `SmartChat Analytics` product documentation
  - Comprehensive white paper on enterprise-grade AI analytics
  - Includes strategic framework and implementation guidelines
  - Covers ROI analysis and deployment best practices

### v1.27.0 (November 6, 2025)
- **New Skill**: Added `new-proposal` for creating professional business proposals
  - Includes AI-powered proposal generation and customization
  - Features comprehensive proposal outline template
  - Supports multiple export formats and version control

### v1.26.0 (November 6, 2025)
- **Documentation Update**: Standardized Work-Day skill reference in `set-up-workday`
  - Updated documentation to consistently use "Work-Day skill" terminology
  - Improved clarity in workflow step descriptions

### v1.25.0 (November 6, 2025)
- **Enhanced Skill**: Updated `set-up-workday` with improved documentation and workflow clarity
  - Refined workspace preparation step in the workflow
  - Clarified skill boundaries and prerequisites
  - Improved integration with Work-Day skill

### v1.24.0 (November 4, 2025)
- **New Skill**: Added `new-quotation` for generating customer quotations using structured templates and pricing inputs
- **Assets**: Added Sentient Quotation Excel template under `new-quotation/templates/`
- **Documentation**: Updated README to include new skill and assets

### v1.23.0 (November 4, 2025)
- **New Idea**: Added `meeting-minutes` skill idea for automated meeting documentation
- **Documentation**: Updated README with latest project status and new skill idea

### v1.22.0 (November 3, 2025)
- **Repository Cleanup**: Removed `project-pulse-brief` idea file from Ideas folder as it's now fully implemented
- **Documentation**: Updated README to reflect current repository state

### v1.21.0 (November 3, 2025)
- **New Skill**: Added `project-pulse-brief` for integrated project tracking and reporting
- **Repository Cleanup**: Removed `set-up-workday` idea file as it's now fully implemented
- **Documentation**: Added project pulse brief template and guidelines
- **Repository Structure**: Added new project-pulse-brief directory with assets

### v1.20.0 (November 3, 2025)
- **Documentation**: Updated README with latest project status
- **Skill Status**: Marked `set-up-workday` as production-ready

### v1.19.0 (November 3, 2025)
- **Skill Enhancement**: Updated `set-up-workday` with improved YAML frontmatter and documentation
- **Bug Fixes**: Resolved YAML parsing issues in skill metadata

### v1.18.0 (November 3, 2025)
- **New Skill Implementation**: Added `set-up-workday` skill implementation with full orchestration
- **Enhanced Workflow**: Integrated the morning intelligence package with Recent Emails, Calendar, and other core skills

### v1.17.0 (November 3, 2025)
- **Enhanced Skill Idea**: Updated `set-up-workday` with workflow and integration details
- **Efficiency Improvements**: Added optimization strategies for skill orchestration
- **Documentation**: Enhanced setup instructions and dependency management

### v1.16.0 (November 3, 2025)
- **New Skill Idea**: Added initial concept for `set-up-workday` skill
- **Repository Structure**: Added new skill idea documentation

### v1.15.0 (November 3, 2025)
- **New Skill**: Added `project-pulse-brief` for integrated project tracking and reporting
- **New Skill**: Added `sentient-proposal-guidelines` for standardized proposal creation
- **Enhanced Skill**: Updated `customer-brief` with comprehensive documentation and use cases
- **Repository Cleanup**: Removed redundant customer brief idea file

### v1.14.0 (November 3, 2025)
- **New Skill**: Added `customer-brief` for generating actionable customer briefs from multiple data sources
- **Enhanced Documentation**: Updated skill structure and usage examples
- **Repository Structure**: Added new customer-brief skill directory with implementation

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
- **new-product**: Added skill for generating enterprise-grade product white papers

### v1.5.0 (October 31, 2025)
- **new-presentation**: Added Steve Jobs-style presentation creation with 3-Second Rule methodology

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
- **set-up-workday**: Comprehensive morning orchestration and executive brief
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

### 📧 **daily-emails**
Unified Gmail skill with 7 sub-commands: recent, starred, actioned, topic, stakeholders, draft, and format. Consolidates email retrieval, drafting, stakeholder monitoring, and executive formatting into a single efficient workflow.

### 📅 **search-calendar**
Search your Google Calendar across multiple dimensions - by day, date, week, subject, attendee names, and emails. Supports flexible natural language queries with fuzzy matching for intelligent results.

### ✏️ **change-headings**
Converts document headings into normal paragraphs while preserving their original visual appearance (font size, weight, color, and formatting). Ideal for normalizing document structure without altering the visual design. Handles all heading levels and maintains inline formatting.

### 🔄 **set-up-workday**
Runs the entire morning activation workflow in one command, including unread email triage, calendar review, Drive activity scan, task synthesis, news snapshot, and workspace preparation. Deduplicates inputs across supporting skills and outputs an executive-format kickoff brief with staged Drive links.

### � **project-pulse-brief** *(Not yet loaded in Claude)*
Curates stakeholder-ready pulse briefs that summarize project portfolio updates, risks, and next steps. Provides a structured approach to project status reporting with reusable templates and checklists. *Note: This skill has been developed but not yet loaded into Claude's active skillset.*

### �📂 **recent-drive**
Lists the most recent files created or modified in Google Drive. Defaults to last 24 hours, or accepts custom timeframe. Returns files with modification dates, summaries, and clickable links sorted by recency.

### 📰 **news-snapshot**
Retrieve and summarize current international and Singapore news stories with headlines, brief context, and source links in a professional executive format. Use when you need a quick daily news briefing with verified sources.

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

### 🎯 **new-presentation**
Create powerful presentations using Steve Jobs's 3-Second Rule methodology. Applies the Billboard Test principles for minimal cognitive load, maximum visual impact, and elegant slide design. Ideal for product launches, pitches, and keynotes that require high audience retention and visual clarity.

### 📄 **new-product**
Generate comprehensive Enterprise AI Product White Papers using existing documentation as source material. Creates authoritative, research-backed documents that educate buyers and present solutions to complex business problems, with a focus on strategic value and ROI for enterprise audiences.

### 🧾 **new-quotation**
Generate customer quotations using a structured template and pricing inputs. Includes a Sentient Quotation Excel template and Markdown template for consistent formatting.

### 📑 **new-proposal** *(Not yet loaded in Claude)*
Create and manage professional sales proposals with AI-powered templates. Features include dynamic content generation, comprehensive case studies, and automated Google Docs output. The skill is optimized for executive audiences with streamlined input requirements and direct Workday integration for document management. *Note: This skill has been developed but not yet loaded into Claude's active skillset.*

### 💰 **smartchat-service-costs** *(Not yet loaded in Claude)*
Analyzes and estimates costs for SmartChat service implementations. Provides cost breakdowns, scenario planning, and ROI calculations for different deployment scales. Includes reference architectures and cost optimization recommendations. *Note: This skill has been developed but not yet loaded into Claude's active skillset.*

### 📂 **Topic Files**
Advanced document management and summarization tool for organizing and analyzing document collections. Features include Google Drive query support, structured summarization, and comprehensive documentation for query operators. Includes a summary checklist for consistent output quality.

### 📄 **list-files**
Generate organized file listings with consistent formatting, metadata, and Google Drive deep links. Includes file type categorization, size indicators, and last modified timestamps. Ideal for creating structured file inventories and document collections.

### 📊 **SmartChat Analytics**
Enterprise-grade AI analytics platform enabling natural language data exploration and insights. Features include semantic data understanding, natural language querying, and explainable AI outputs. Comprehensive white paper available in the products directory.

### 🔍 **recent-files**
Track and analyze recent Google Drive activity with detailed metadata and insights. Features include chronological work narratives, activity patterns, project focus areas, and client-specific tracking. Ideal for reviewing work history, tracking project progress, and maintaining awareness of team activities.

## Folder Structure

```
/
├── daily-emails/           # Unified Gmail skill (recent, starred, drafting, stakeholders)
│   └── skill.md           # Skill implementation
├── search-calendar/        # Google Calendar search skill
│   └── skill.md           # Skill implementation
├── recent-drive/           # Google Drive file discovery skill
│   └── skill.md           # Skill implementation
├── news-snapshot/          # News briefing skill
│   └── skill.md           # Skill implementation
├── set-up-workday/       # Morning orchestration and executive brief skill
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
├── new-presentation/      # Steve Jobs-style presentations
│   └── skill.md          # Skill implementation
├── new-product/           # Enterprise white paper generation
│   ├── references/       # White paper templates and guidelines
│   └── skill.md          # Skill implementation
├── new-quotation/         # Quotation generation skill
│   ├── templates/
│   │   ├── sentient-quotation-template.md
│   │   └── Sentient Quotation Template.xlsx
│   └── skill.md          # Skill implementation
├── new-proposal/         # Business proposal generation
│   ├── proposals/
│   │   └── SmartChat-Analytics.md  # Enterprise AI Analytics White Paper library
│   ├── templates/
│   │   └── proposal-outline.md  # AI Sales Proposal Outline
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
