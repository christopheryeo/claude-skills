# Claude Skills Library

## Overview

A collection of custom Claude skills that extend Claude's capabilities with specialized workflows for the Sentient.io AI Workforce. Covers productivity, email management, calendar operations, document creation, information retrieval, and daily operations. Each skill is a self-contained folder with a SKILL.md definition file.

## Architecture

Each skill lives in its own sub-folder containing a `SKILL.md` file (the skill definition) and optional supporting files (templates, reference data, examples). Skills are loaded into Claude via the Cowork skills system and triggered by natural language patterns defined in their descriptions. Some skills are "micro-skills" (e.g. `list-files`, `list-emails`) designed to be called by other skills for consistent formatting.

## Current Status

v1.36.1 (December 2025). 30+ active skills covering daily operations, email, calendar, document creation, presentations, stakeholder monitoring, and development workflows. Maintained by Christopher Yeo and Alex.

## Contacts & Stakeholders

| Name | Role | Contact |
|---|---|---|
| Christopher Yeo | CEO / Project Owner | chris@sentient.io |

## Learned Preferences

### Skill Architecture — Native Connector First + Delegation Hierarchy
Fundamental skills (`daily-emails`, `daily-calendars`, `daily-files`) own connector policy and output formatting. Higher-order skills must always delegate to them — never call connectors directly. See full policy: [`Knowledge/skill-architecture-policy.md`](Knowledge/skill-architecture-policy.md).
