# daily-calendars Skill — Evaluation Report
**Date:** 2026-03-06
**Evaluator:** Claude (automated eval)
**Skill Version:** As defined in `/daily-calendars/SKILL.md`
**Evaluation Criteria:** Overall quality — accuracy, format, completeness

---

## Summary Verdict

| Scenario | Description | Pass/Fail | Notes |
|---|---|---|---|
| 1 | Today's events | ✅ Pass | Clean output, correct date scoping |
| 2 | Search by attendee name (Mani) | ✅ Pass (with caveat) | Correct results; required overflow file handling |
| 3 | Search by title keyword (standup) | ✅ Pass | Server-side `q=` filter used efficiently |
| 4 | Specific date lookup (March 10) | ✅ Pass | Correct scoping; noted scheduling conflict |
| 5 | This week's meetings | ✅ Pass | Correct week scoping; good volume handling |

**Overall: ✅ PASS** — The skill performs correctly and reliably across all five tested scenarios. Minor issues noted below.

---

## Scenario Results

### Scenario 1: Today's Events
**Query:** "What do I have on today?"
**Time filter:** 2026-03-06 (full day, Asia/Singapore)
**Result count:** 4 meaningful events (after filtering all-day "Home" working location markers)

**Accuracy:** ✅ Correctly identified today's date and scoped the query accordingly.
**Format:** ✅ Table output with title, time, duration, attendees, and prep flag was clear and scannable.
**Completeness:** ✅ All relevant events returned. Working location markers correctly excluded from display.

---

### Scenario 2: Search by Attendee Name
**Query:** "Find meetings with Mani"
**Time filter:** Next 30 days (default)
**Result count:** 10 meetings matched across 4 recurring series

**Accuracy:** ✅ Correct attendee match against `mani@sentient.io`. Fuzzy name resolution worked.
**Format:** ✅ Results well-grouped and readable.
**Completeness:** ✅ All relevant meetings returned.
**Issue:** ⚠️ The raw API response (87,128 characters) exceeded the in-context token limit. Required reading from an overflow temp file and applying a Python/jq filter to extract matching events. This is a robustness concern for large calendar datasets — the skill SKILL.md does not currently document a fallback strategy for this case.

---

### Scenario 3: Search by Title Keyword
**Query:** "Find any standup meetings in the next 30 days"
**Time filter:** Next 30 days
**Result count:** 4 instances of "Tampines Project Standup" recurring series

**Accuracy:** ✅ Server-side `q=standup` parameter used, returning only relevant events without client-side post-filtering overhead.
**Format:** ✅ Clean table output with recurring event instances clearly listed.
**Completeness:** ✅ All standup instances in the window returned.

---

### Scenario 4: Specific Date Lookup
**Query:** "What's on my calendar on March 10?"
**Time filter:** 2026-03-10 (full day, Asia/Singapore)
**Result count:** 3 meaningful events (excluding working location marker)

**Accuracy:** ✅ Correct date scoping. Correctly identified a scheduling conflict between "Corp Dev Huddle" and "Tampines Project Standup" (the standup was already declined, so no action needed — appropriately flagged).
**Format:** ✅ Table output. RSVP status included, which was critical for interpreting the conflict.
**Completeness:** ✅ All events returned and context was well-presented.

---

### Scenario 5: This Week's Meetings
**Query:** "Show me all my meetings this week"
**Time filter:** Mon 2026-03-02 to Fri 2026-03-06
**Result count:** 19 raw entries → 11 substantive meetings after filtering working location events

**Accuracy:** ✅ "This week" correctly interpreted as the current calendar week (Mon–Fri). Not shifted to next week or last week.
**Format:** ✅ Events grouped chronologically across all 5 weekdays. Readable and well-structured.
**Completeness:** ✅ Full week coverage including recurring series (standups, 1:1s, team syncs).

---

## Issues and Observations

### Issue 1: Token Overflow on Large Date Ranges (Medium Priority)
**Observed in:** Scenario 2 (30-day attendee search)
**Description:** When querying 30 days of events across all calendars, the `gcal_list_events` response can exceed in-context token limits (~87K characters). The skill's SKILL.md does not document a fallback for this case.
**Recommendation:** Add a fallback note to SKILL.md instructing Claude to read the overflow file from the tool-results temp path and apply a Python/jq filter when the response is truncated. Alternatively, consider paginating or reducing the default window for attendee searches.

### Issue 2: Working Location Events Not Auto-Filtered (Low Priority)
**Observed in:** Scenarios 1, 4, 5
**Description:** All-day events titled "Home" (or similar working location markers) appear in raw API results and must be manually excluded before presenting to the user. This filtering was applied correctly each time, but it relies on Claude's inference rather than an explicit rule in the skill.
**Recommendation:** Add a note to SKILL.md: "Exclude all-day events with titles matching working location keywords (Home, Office, Remote, WFH) from displayed results."

### Issue 3: No `myResponseStatus` Field in Output (Low Priority)
**Observed in:** Scenarios 4, 5
**Description:** The skill's output contract does not include a `myResponseStatus` field (i.e., Chris's own RSVP status). In Scenario 4, the declined standup was only identifiable because the attendee list showed `response_status: declined` for Chris's entry — requiring cross-referencing. A top-level `myResponseStatus` field would make this immediately visible.
**Recommendation:** Add `myResponseStatus` to the output contract JSON schema in SKILL.md for quick filtering by the user's own response status.

---

## Strengths

- **Natural language date parsing** is robust — "today", "this week", and "March 10" all resolved correctly.
- **Attendee fuzzy matching** worked well for first-name-only input ("Mani" → `mani@sentient.io`).
- **Server-side `q=` filtering** used intelligently for title keyword searches, reducing payload size.
- **prep_needed enrichment** correctly flagged events with conferencing, large attendee counts, or doc links.
- **Timezone normalization** (Asia/Singapore) was consistently applied.
- **Conflict detection** was surfaced naturally in Scenario 4 without being explicitly prompted.

---

## Recommendations Summary

| Priority | Recommendation |
|---|---|
| Medium | Document overflow fallback in SKILL.md for large API responses |
| Low | Add explicit filter rule for working location events |
| Low | Add `myResponseStatus` to output contract schema |

---

*Evaluation completed: 2026-03-06*
