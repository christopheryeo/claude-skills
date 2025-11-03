---
name: project-pulse-brief
description: Curate stakeholder-ready pulse briefs that summarize project portfolio updates, risks, and next steps.
license: Complete terms in LICENSE.txt
version: 1.1.1
author: OpenAI Codex
created: 2024-03-09
keywords: project status, portfolio reporting, executive brief, markdown
---

# Project Pulse Brief

## Overview
Project Pulse Brief is a lightweight playbook for turning raw project status
updates into an executive-ready pulse brief. The skill focuses on repeatable
steps, reusable checklists, and a template you can copy into any document or
collaboration space. No scripts, bots, or external integrations are required.

## Quick Start
1. Gather weekly status inputs from project leads (email, docs, or meetings).
2. Consolidate details using the intake prompts in
   `references/configuration.md` to ensure every project includes summary,
   health, blockers, and next steps.
3. Open `assets/templates/pulse_brief_template.md` and duplicate it in your
   preferred editor or knowledge base.
4. Populate each section with the curated inputs, referencing
   `references/configuration.md` for recommended section order and labeling.
5. Share the completed brief with stakeholders via your usual communication
   channels (email, workspace doc, meeting deck, etc.).

## What This Skill Provides
- **Repeatable workflow** for consolidating project updates each reporting
  cycle.
- **Editable template** that keeps highlights, blockers, and upcoming work in a
  consistent structure.
- **Curation checklist** to maintain quality: confirm owner, dates, status, and
  key decisions before publishing.

## What This Skill Does NOT Provide
✗ Automated data ingestion from portfolio tools.  
✗ Command-line utilities or runtime scripts.  
✗ Direct integrations with chat platforms or email services.

## Recommended Workflow
1. Collect updates asynchronously using the intake prompts outlined in
   `references/configuration.md`.
2. During a short review session, triage updates into highlights, watchlist, and
   risks using the prompts in `references/configuration.md`.
3. Populate the markdown template with the agreed priorities. Use callouts or
   bolding (see template) to emphasize decisions and support requests.
4. Capture follow-up actions in a shared tracker so the next brief can close the
   loop on open items.

## Success Criteria
- Every project entry lists owner, current status, recent wins, blockers, and
  next steps.
- Sponsors can skim the brief and understand portfolio health within two
  minutes.
- Follow-up actions from the previous pulse are either completed or reprioritized
  in the new brief.

## Roles & Responsibilities
- **Brief Curator**: Coordinates intake, validates completeness, and drafts the
  pulse brief.
- **Project Leads**: Provide weekly updates aligned to the required fields.
- **Executive Sponsor**: Reviews the brief for alignment and approves
  distribution.

## Guardrails
- Keep the brief under two pages to preserve executive readability.
- Highlight no more than five items per section; link to supplemental docs for
  deep dives.
- Use neutral, objective tone—avoid speculative language without data backing.
- Document open risks with clear owners and mitigation dates.

## Troubleshooting
Consult `references/troubleshooting.md` for guidance when data is incomplete,
conflicting, or submitted late. It includes reminder language and escalation
paths to keep the reporting cadence on track.

## Related Skills
- **morning-recon-brief**: Pair with Project Pulse Brief for a wider view of
  operational signals plus delivery progress.
- **recent-files**: Helps locate supporting artifacts referenced in the pulse
  brief.

## Version History
- **1.1.1** (2024-03-12): Removed the project update worksheet in favor of
  lightweight intake prompts embedded in the configuration guide.
- **1.1.0** (2024-03-11): Simplified into a documentation-first workflow without
  CLI tooling or chat integrations.
- **1.0.0** (2024-03-09): Initial release with automation scripts.
