# Skill Creation Manifest: topic-emails

## Context and Design Process
This manifest follows the guidance in `references/instructions.md`, using the existing Gmail-focused skills (`recent-emails`, `starred-email`, and `actioned-emails`) as structural references. The goal is to graduate the `Ideas/topic-emails.md` concept into a production-ready Claude skill.

## Overview
Deliver a focused Gmail briefing that rounds up every thread related to a requested topic. The skill builds precise Gmail searches using keywords, timeframe filters, and label exclusions, then expands each thread for summaries, metadata, and deep links so the user can brief stakeholders or resume conversations instantly.

## Success Criteria and Guard Rails
- **Success looks like:**
  - Captures required inputs (topic, timeframe, exclusions, participants) before querying.
  - Uses `search_gmail_messages` plus `read_gmail_thread` to retrieve metadata and full context.
  - Documents the exact Gmail query in the response for transparency.
  - Highlights the top three threads, then provides a comprehensive table of remaining matches.
  - Localizes timestamps and includes Gmail deep links for each thread.
- **Guard rails:**
  - Never fabricate messages or participants—report only Gmail results.
  - Respect label exclusions and avoid modifying user data (read-only behavior).
  - Handle empty, partial, or oversized result sets with clear guidance on next steps.
  - Surface integration failures transparently and suggest remediation.

## Step 1: Create Directory Structure
```bash
mkdir -p topic-emails/references
```

## Step 2: Create `topic-emails/skill.md`
Copy the content from the main specification (see repository) into `skill.md`. It includes YAML front matter, usage guidance, inputs, query construction, execution steps, output template, special-case handling, guard rails, and related skills.

## Step 3: References
This manifest is the only reference document required. No additional configuration guides or troubleshooting docs are needed for launch.

## Step 4: Assets
No assets or templates are required. Do not add files under `assets/` for this skill.

## Validation & Next Steps
- Confirm `topic-emails/skill.md` matches the committed specification.
- Test prompt variants like "Gather all emails about Project Atlas last quarter" to ensure the skill requests clarifying inputs and reports results in the defined structure.
- Revisit after user feedback to expand export automation (e.g., generating CSVs automatically) or to add integrations beyond Gmail if needed.
