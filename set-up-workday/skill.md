---
name: set-up-workday
description: Orchestrates the morning startup stack by chaining existing skills to brief the principal, stage Drive folders, and surface top priorities for the workday.
license: Proprietary
version: 1.0.0
author: SNMG Chief of Staff Team
created: 2025-11-03
keywords: morning,workflow,orchestration,briefing
---

# Set Up Workday

## Overview
Set Up Workday is a meta-orchestration skill that activates the full morning enablement stack for the SNMG organization. It coordinates existing reconnaissance, communications, calendar, and workspace preparation skills to assemble a ready-to-execute briefing for the selected workday. Invoke it whenever the principal needs an actionable morning package without touching multiple tools manually.

## Quick Start
1. Receive the user prompt (e.g., "Set up my workday" or "Kick off today using our standard morning stack").
2. Confirm the target date (default to today) and any optional toggles such as skipping email checks or focusing on specific accounts.
3. Execute the dependency chain, collate the results into a structured kickoff brief, and return prioritized actions, schedule snapshot, and Drive workspace links.

## How It Works
1. **Determine target date** using Reverse Date and Reverse Month to normalize formatting for downstream skills and folder naming.
2. **Collect situation report** by calling Morning Recon Brief, Recent Emails, and Starred Email, passing include_email flags and message IDs to prevent duplicate pulls.
3. **Review schedule** via Search Calendar with time_min/time_max bounded to the workday window for agendas, prep documents, and participants.
4. **Resume context** with Recent Files, scoped to the last 48 hours and aligned to the normalized date to surface in-progress work.
5. **Prepare workspace** by invoking Work Day in dry run mode first, then committing folder creation if the structure is missing.
6. **Synthesize plan** that merges all inputs, deduplicates overlapping items, and highlights top priorities, urgent follow-ups, and quick wins.
7. **Deliver output** formatted as an executive kickoff brief covering priorities, schedule, follow-ups, workspace links, and reminders.

## Key Features
- **End-to-end orchestration**: Chains seven existing Claude skills into a single predictable workflow.
- **Data de-duplication**: Reuses identifiers between skills to avoid redundant email or calendar lookups.
- **Workspace readiness**: Verifies Google Drive structures for the day and stages links for immediate access.
- **Configurable toggles**: Supports skip flags (email, calendar) and account-specific focus modes for flexible mornings.

## Success Criteria
**The skill succeeds when:**
- The orchestrator executes the dependency chain without redundant API calls or conflicting outputs.
- The final brief includes prioritized actions, urgent follow-ups, schedule snapshot, workspace links, and quick wins tied to the requested date.
- Users receive actionable recommendations with traceable sources for every item in the summary.

## What This Skill Does
✓ Activates the standard morning stack from a single command.
✓ Normalizes target dates and reuses them across calendar, files, and Drive preparation.
✓ Produces an executive-format kickoff brief with clear sections and links.

## What This Skill Does NOT Do
✗ Replace the underlying skills’ authentication or permission flows.
✗ Invent new data sources beyond the defined dependency list.
✗ Auto-schedule focus blocks or push tasks into external project managers (future consideration).

## Limitations & Prerequisites
- **Requires**: Access to Morning Recon Brief, Recent Emails, Starred Email, Search Calendar, Recent Files, Reverse Date, Reverse Month, and Work Day skills with valid integrations.
- **Assumes**: Google Workspace connectivity, consistent timezone handling (default Asia/Singapore), and cached credentials for Gmail, Calendar, and Drive.
- **Limitations**: Does not currently integrate Asana/Jira task queues; brief delivery format is Markdown rendered within Claude unless extended.

## Usage

### Basic Usage
```
User: "Set up my workday."
Assistant: Runs the full orchestration, returning the briefing for today.
```

### Advanced Usage
```
User: "Prepare everything I need for work this morning for 2025-11-04. Skip email, focus on APAC enterprise accounts."
Assistant: Normalizes the provided date, toggles off email checks, scopes downstream skills to APAC enterprise filters, and delivers the kickoff brief.
```

### Configuration
- Optional flags: `include_email` (bool), `focus_accounts` (list of strings), `time_window` (start/end timestamps), `dry_run_folders` (bool).
- Cache normalized dates and folder IDs within the session to prevent repeated computations.

## Scripts

### Orchestrator: `scripts/set_up_workday.py`
**Purpose**: Placeholder for the automation layer that sequences dependency skills, manages state, and formats the final brief.
**Status**: Not yet implemented; use this specification to guide future development.
**Expected Responsibilities**:
- Handle prompt parsing and configuration toggles.
- Execute dependency calls with shared identifiers (message IDs, event IDs, folder IDs).
- Deduplicate overlapping items and assemble the final briefing template.

## Integration Opportunities

### Asana or Jira Task Sync
**Purpose**: Pull outstanding tasks and optionally create follow-up tasks from the morning brief.
**Proposed Implementation**: Optional step after synthesizing the plan that queries project management APIs for blockers or logs new action items.
**Prerequisites**: API credentials with write access, project mappings per account or initiative.
**Usage Context**: Enable when the principal wants workday setup to include outstanding project tasks.

### Slack Notifications
**Purpose**: Deliver the final kickoff brief to a private Slack channel for archival and quick reference.
**Proposed Implementation**: Post-brief webhook call with formatted Markdown and key links.
**Prerequisites**: Slack app with chat:write scope and channel ID configuration.
**Usage Context**: Teams needing asynchronous distribution of the morning setup output.

## Related Skills
- **morning-recon-brief**: Supplies overnight news, inbox highlights, and situational awareness.
  - *This skill differs by*: Orchestrating multiple skills and producing the final kickoff plan.
  - *Can be used together with*: Use Morning Recon Brief as the first dependency to avoid duplicate fetches.
- **recent-emails** and **starred-email**: Provide actionable email threads and context.
  - *This skill differs by*: De-duplicating and highlighting next actions across inbox feeds.
  - *Can be used together with*: Feed thread IDs between these skills for deeper metadata lookups.
- **work-day**: Ensures Google Drive folder structure is ready.
  - *This skill differs by*: Triggering Work Day’s checks as part of the morning orchestration.

## Extending This Skill
To extend Set Up Workday with new capabilities:
1. Implement `scripts/set_up_workday.py` following the orchestration responsibilities above.
2. Add optional integrations (e.g., task managers) and document configuration steps under a new `references/` guide.
3. Update this SKILL.md with additional usage patterns and toggle descriptions as features roll out.

## Common Issues

**Issue**: Missing permissions for Gmail or Calendar during dependency calls.
**Solution**: Re-authenticate the corresponding skills and ensure OAuth scopes include read access for messages and events.

**Issue**: Duplicate follow-up items appearing in both Recent Emails and Starred Email sections.
**Solution**: Use message IDs returned by Starred Email to filter Recent Emails responses before synthesizing the plan.

**Issue**: Work Day reports folders already exist but links are missing from the final brief.
**Solution**: Cache folder IDs returned from Work Day and explicitly inject them into the Active Docs & Resources section before rendering.

## Version History
- **1.0.0** (2025-11-03): Initial specification for the Set Up Workday orchestration skill, outlining workflow, dependencies, and integration opportunities.
