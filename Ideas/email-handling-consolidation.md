# Email Handling Skill Consolidation — Feasibility Report

**Date:** 2026-02-28
**Author:** Alex (Dev)
**Status:** Exploration / Idea

---

## Objective

Evaluate whether the seven existing email-related skills can be consolidated into a single `email-handling` skill with sub-commands, and what the trade-offs would be.

---

## Current Email Skills Inventory

| # | Skill | Lines | Purpose | Type |
|---|-------|-------|---------|------|
| 1 | **recent-emails** | ~146 | List recent emails across all folders (Inbox, Sent, Drafts, Starred) | Retrieval |
| 2 | **starred-email** | ~97 | Surface starred/priority emails with action notes | Retrieval |
| 3 | **actioned-emails** | ~110 | Blend sent + starred into an executive recap | Retrieval |
| 4 | **topic-emails** | ~119 | Search emails by topic/keyword across time | Retrieval |
| 5 | **monitor-stakeholders** | ~113 | Scan Gmail for emails from tracked contacts | Retrieval + External data |
| 6 | **draft-email** | ~122 | Draft reply-all emails and save to Gmail drafts | Action (write) |
| 7 | **list-emails** | ~136 | Format email metadata into executive tables | Formatter (micro-skill) |

**Total:** ~843 lines across 7 skills

---

## Dependency Map

```
recent-emails ──────→ list-emails
starred-email ──────→ list-emails
actioned-emails ────→ list-emails
topic-emails ───────→ (standalone formatting)
monitor-stakeholders → list-emails + Knowledge/Stakeholder_Monitoring.md
draft-email ────────→ (standalone, no formatter dependency)
```

All retrieval skills except `topic-emails` and `draft-email` depend on `list-emails` as a downstream formatter. `monitor-stakeholders` also depends on an external stakeholder list file.

---

## Overlap Analysis

### High Overlap

| Area | Skills involved | What's duplicated |
|------|----------------|-------------------|
| Gmail query construction | recent-emails, starred-email, actioned-emails, topic-emails, monitor-stakeholders | All five build Gmail queries with time filters, deduplication logic, and result limits |
| Thread reading strategy | recent-emails, starred-email, actioned-emails, topic-emails, monitor-stakeholders | All five have token-optimization logic for when to read full threads vs. message metadata |
| Summary generation | All retrieval skills | 25–35 word summary rules repeated in each |
| Gmail link construction | All retrieval skills + list-emails | `https://mail.google.com/mail/u/0/#folder/message_id` pattern repeated everywhere |
| Guard rails | All 7 skills | "Never fabricate", "timezone aware", "integration failures" boilerplate in every skill |

### Low Overlap / Unique Logic

| Skill | Unique capability |
|-------|-------------------|
| **monitor-stakeholders** | Reads external `Stakeholder_Monitoring.md`, groups results by stakeholder category, applies monitoring rules |
| **draft-email** | Composes HTML replies, determines reply-all recipients, creates Gmail drafts — entirely different from retrieval |
| **topic-emails** | "Spotlight Threads" format, relevance scoring, export guidance |
| **actioned-emails** | Dual-window concept (24h sent + 7d starred), merge logic |
| **list-emails** | Pure formatter — no Gmail API calls, receives pre-processed data |

---

## Proposed Sub-Command Architecture

### Option A: Full Consolidation (all 7 → 1 skill)

```
email-handling
├── recent      — List recent emails (replaces recent-emails)
├── starred     — Surface starred emails (replaces starred-email)
├── actioned    — Sent + starred recap (replaces actioned-emails)
├── topic       — Topic-based search (replaces topic-emails)
├── stakeholders — Stakeholder monitoring (replaces monitor-stakeholders)
├── draft       — Draft reply emails (replaces draft-email)
└── (built-in)  — list-emails formatting absorbed as shared output layer
```

**Trigger detection:** Skill description would need to match all current trigger phrases. Sub-command routing would be handled by a detection table at the top of the skill, similar to how `daily-plans` routes between CREATE/EXECUTE/LOG/STATUS/DELETE/CARRY-FORWARD.

### Option B: Partial Consolidation (retrieval skills only)

```
email-handling
├── recent      — List recent emails
├── starred     — Surface starred emails
├── actioned    — Sent + starred recap
├── topic       — Topic-based search
└── (built-in)  — list-emails formatting absorbed

Remain separate:
├── monitor-stakeholders (depends on external stakeholder data)
├── draft-email (write action, fundamentally different from retrieval)
```

### Option C: Keep Separate, Extract Shared Library

```
email-common/           ← new shared module
├── query-builder       — Gmail query construction helpers
├── thread-reader       — Token-optimized reading strategy
├── deduplication       — Cross-folder message dedup
├── link-generator      — Gmail deep link construction
├── guard-rails         — Standard safety/quality boilerplate
└── list-emails         — Formatting (already exists)

Individual skills import from email-common/ instead of duplicating logic.
```

---

## Trade-Off Assessment

| Criteria | Option A (Full) | Option B (Partial) | Option C (Shared Lib) |
|----------|:-:|:-:|:-:|
| **Lines reduced** | ~843 → ~500 (est.) | ~843 → ~600 (est.) | ~843 → ~700 (est.) |
| **Trigger accuracy** | ⚠️ Risk — single description must cover 7 use cases | ✅ Good — 5 related use cases, 2 distinct skills kept | ✅ Best — each skill keeps its own triggers |
| **Skill file size** | ⚠️ ~500 lines (at the 500-line limit) | ✅ ~350 lines + 2 separate skills | ✅ Each skill stays small |
| **Maintenance** | ✅ Single file to update | ✅ Mostly single file | ⚠️ Must maintain shared module + individual skills |
| **Sub-command routing** | ⚠️ Complex — must detect 7 intents | ✅ Moderate — 5 related intents | N/A — no routing needed |
| **Risk of misfire** | ⚠️ High — "draft a reply" vs "show recent" vs "monitor stakeholders" are very different intents | ✅ Lower — retrieval intents are related | ✅ Lowest — no change to triggers |
| **Cowork skill limit** | ✅ Reduces skill count by 6 | ✅ Reduces by 4 | ❌ No reduction (may increase by 1) |
| **Follows daily-plans pattern** | ✅ Yes — proven sub-command model | ✅ Yes | ❌ Different pattern |

---

## Recommendation

**Option B (Partial Consolidation)** is the best balance of benefit and risk:

1. **Consolidate the 4 retrieval skills** (recent-emails, starred-email, actioned-emails, topic-emails) + **absorb list-emails** as the internal formatter into a single `email-handling` skill with sub-commands: `recent`, `starred`, `actioned`, `topic`.

2. **Keep `monitor-stakeholders` separate** — it has a fundamentally different input source (external stakeholder file) and serves a distinct workflow. It can still call the consolidated skill's formatting layer.

3. **Keep `draft-email` separate** — it's a write action, not a retrieval skill. Mixing read and write operations in one skill increases misfire risk and makes the description harder to write.

**Result:** 7 skills → 3 skills (email-handling, monitor-stakeholders, draft-email), with shared formatting built in.

---

## Estimated Implementation Effort

| Step | Effort |
|------|--------|
| Design sub-command routing table | ~30 mins |
| Merge retrieval logic with shared query builder | ~1 hour |
| Absorb list-emails as internal formatter | ~30 mins |
| Write unified skill description for trigger accuracy | ~30 mins |
| Update monitor-stakeholders to reference new skill | ~15 mins |
| Testing all 4 sub-commands | ~1 hour |
| **Total** | **~3.5 hours** |

---

## Next Steps

1. Review this report and decide on Option A, B, or C
2. If Option B approved, create `email-handling/skill.md` skeleton with sub-command routing
3. Migrate retrieval logic skill-by-skill, testing each sub-command
4. Update skill descriptions and Cowork registration
5. Archive retired individual skill folders

---

*Generated: 2026-02-28*
