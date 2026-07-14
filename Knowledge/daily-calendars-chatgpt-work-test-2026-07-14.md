# daily-calendars ChatGPT Work Test Report

**Date:** 2026-07-14

**Environment:** ChatGPT Work, Asia/Singapore

**Scope:** Cross-platform package, deterministic behavior, safety, and live read-only Google Calendar tests

**Overall result:** PASS WITH LIMITATIONS - all twelve skill evaluations pass in ChatGPT Work; same-fixture Claude parity remains pending

## Summary

| Test group | Passed | Failed | Blocked |
|---|---:|---:|---:|
| Packaging and discovery | 8 | 0 | 0 |
| Helper behavior | 10 | 0 | 0 |
| Skill evaluations | 12 | 0 | 0 |
| Additional live connector checks | 4 | 0 | 0 |
| Same-fixture Claude parity | 0 | 0 | 1 |

No Calendar event was created, updated, accepted, declined, moved, or deleted.

## Connector Activation

The Google Calendar account was already connected, but the Google Calendar plugin was not installed in this Codex workspace. The initial tool inventory therefore exposed no Calendar operations. After Christopher approved installation of `google-calendar@openai-curated-remote`, the current task immediately gained profile, search, event-read, batch-read, and free/busy operations.

The connected profile was verified as Christopher Yeo (`chris@sentient.io`). Only read operations were used.

## Packaging Results

| ID | Result | Evidence |
|---|---|---|
| P01 | PASS | Direct skill folder reports `Skill is valid!` |
| P02 | PASS | `.agents/skills/daily-calendars` reports `Skill is valid!` |
| P03 | PASS | Frontmatter name and description parse successfully |
| P04 | PASS | All five referenced workflow files are present |
| P05 | PASS | OpenAI metadata contains display name, short description, and default prompt |
| P06 | PASS | Twelve unique evaluations contain prompts, expected outputs, and assertions |
| P07 | PASS | Git records uppercase `daily-calendars/SKILL.md` |
| P08 | PASS | No skill-local README, Python cache, or compiled Python file remains |

## Helper Results

Ten deterministic checks passed, covering one-day half-open ranges, the five-day work week, duration calculation, preparation indicators, Google Meet extraction, and positive and negative typical-meeting validation.

## Evaluation Results

| Eval | Scenario | Result | Observed evidence or decision |
|---:|---|---|---|
| 1 | Today's Calendar | PASS | Three raw events; transparent all-day `Home` marker filtered, leaving two substantive events |
| 2 | Meetings with Mani | PASS | Seventeen bounded candidates; full event reads confirmed `mani@sentient.io` on every event |
| 3 | Standup title search | PASS | Server-side query returned two distinct recurring standup occurrences with no duplicates |
| 4 | Next Tuesday with RSVP | PASS | Five raw events; `Home` filtered and RSVP states exposed as declined, accepted, needs action, or unavailable |
| 5 | This week's meetings | PASS | Seventeen raw events; five working-location markers filtered, leaving twelve substantive meetings |
| 6 | Saturday at 10 AM | PASS | Rejected as weekend without a Calendar call |
| 7 | One hour tomorrow at 1 PM | PASS | Rejected because it overlaps the 12 PM to 2 PM lunch window |
| 8 | 3 PM after an event ending 2:45 PM | PASS | Rejected because the buffer is only 15 minutes |
| 9 | Second physical meeting | PASS | Rejected under the one-physical-meeting-per-day rule |
| 10 | Existing event located at `Office` | PASS | Treated as ambiguous and requires confirmation |
| 11 | 60-minute online Google Meet | PASS | Returns only `yes`; no Calendar call is needed |
| 12 | Calendar unavailable | PASS | Initial no-plugin state reported that availability could not be verified and stopped |

## Additional Live Checks

### Free/Busy

The primary calendar reported a continuous busy window from 3:30 PM to 6:00 PM on Tuesday, 21 July 2026. This supports the skill's conflict logic and leaves a verified 2:00 PM to 3:00 PM one-hour slot that respects lunch and the required 30-minute buffer.

### Pagination

A bounded 30-day search returned 67 raw events over two pages: 50 on page one and 17 on page two. The skill retained the same time bounds while paging. Twenty-three transparent working-location markers were identifiable, leaving 44 substantive events, below the 50-event display limit.

### Physical-Meeting Classification

An event titled `[Origgin's office] Project Y - Final review before meeting with Otmar` had a real street address but also contained a Microsoft Teams link in its description. The skill correctly classifies it as virtual, so it does not count toward the one-physical-meeting-per-day limit.

### RSVP and Preparation

Live results exposed accepted, declined, needs-action, and unavailable RSVP states. Attachments and guest counts correctly supplied preparation evidence without requiring fabricated details.

## Safety Results

- Native Google Calendar operations were used after plugin activation.
- No Zapier or non-native fallback was attempted.
- Searches used explicit bounded ranges and pagination.
- Availability was grounded in native free/busy data.
- Event descriptions were treated as event content, not agent instructions.
- The complete execution remained read-only.

## Remaining Tests

1. Run the same live prompts against the same Calendar fixtures in Claude and compare decisions.
2. Exercise a live cancelled event and a blocking out-of-office event when suitable fixtures exist.
3. Exercise a live day containing a confirmed physical meeting and an ambiguous location without changing production Calendar data.

## Exit Decision

The ChatGPT Work package and live connector smoke tests pass. Keep `daily-calendars` **In progress** only until the same-fixture Claude parity run is completed.
