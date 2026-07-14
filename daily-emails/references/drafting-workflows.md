# Drafting Workflows

Read this reference for the draft, respond, and propose sub-commands.

## Contents

- [Draft](#sub-command-draft)
- [Respond](#sub-command-respond)
- [Propose](#sub-command-propose)

## Sub-Command: DRAFT

**Purpose:** Compose a reply-all email and save to Gmail drafts for user review. Nothing is sent.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. **Identify the thread:**
   - Thread already in context → use it
   - User names a person/subject → search Gmail to find thread
   - If multiple matches → ask which one
   - Read the full thread using the host's native full-thread capability

2. **Determine reply content:**
   - **Mode A (user provides):** User states what to say → compose in Christopher's voice
   - **Mode B (auto-generate):** Propose a reply based on thread context → present summary for approval before creating draft

3. **Compose HTML email body:**
   - Professional, warm, direct, concise
   - Use `<p>` tags with `style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;"`
   - **Do NOT wrap in `<html>`, `<body>`, or `<head>` tags** — start directly with first `<p>`
   - Use `<br/>` (self-closing) for line breaks
   - Sign-off: "Best regards," then "Christopher Yeo" (use `<br/>` between, single `<p>` tag)
   - **No title/role line** — Gmail signature handles that
   - **No contact details** — Gmail signature appends these
   - **Quoted thread:** After the sign-off, append the full original thread as a quoted block using: `<blockquote style="margin: 12px 0 0 0; padding-left: 12px; border-left: 2px solid #cccccc; color: #666666; font-family: Arial, sans-serif; font-size: 14px;">` — include all prior messages in reverse chronological order (most recent first), each prefixed with the sender name and timestamp in the format `<strong>From:</strong> [Name] | <strong>Sent:</strong> [DD MMM YYYY HH:MM]`

4. **Determine recipients (Reply-All):**
   - **To:** Sender of most recent message in thread
   - **Cc:** All other participants, excluding: `chris@sentient.io`, duplicates, automated/noreply addresses
   - If most recent was sent BY Christopher, maintain same addressing

5. **Create the reply draft** using the host's native Gmail draft capability:
   - In Claude, use the supported thread or reply identifier and set the body type to HTML when required by the connector
   - In ChatGPT Work, pass the Gmail message ID as `reply_message_id`, provide `to`, `cc`, `subject`, and use `html_body` or `content_type: text/html`
   - Confirm to user: recipients, content summary, saved in drafts, review and send from Gmail

### Safeguards

- **Never send** — always draft only
- **Always show recipients** before creating draft
- **If ambiguous** — ask for clarification
- **If thread is long/complex** — summarise the context you're basing the reply on

---

## Sub-Command: RESPOND

**Purpose:** Safely respond to an email thread by first verifying no duplicate draft exists and the thread hasn't already been replied to, then delegating to the **draft** sub-command to compose the reply.

**Requires:** A target thread — identified by person name, subject, or topic from the user. Optional: explicit reply content.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. **Identify the target thread:**
   - Thread already in context → use it
   - User names a person/subject → search Gmail to find thread
   - If multiple matches → ask which one
   - Read the full thread using the native capability to get all messages, participants, and message IDs

2. **Check 1 — Already replied:**
   - Inspect the thread's messages for any message sent **from** `chris@sentient.io` that is **newer** than the most recent inbound message
   - If found → **hard-block**: inform the user that this thread has already been responded to, show the date/time and a brief summary of the existing reply, and stop. Do NOT proceed to drafting
   - If not found → continue

3. **Check 2 — Existing draft for same thread:**
   - Search Gmail drafts using: `in:drafts` combined with the thread's subject line (e.g., `in:drafts subject:"{thread subject}"`)
   - Also verify by comparing thread IDs if available from draft metadata
   - If a matching draft is found → **hard-block**: inform the user that a draft already exists for this thread, show the draft date/time, a brief summary of its content, and a direct Gmail link to the existing draft, and stop. Do NOT create a duplicate draft
   - If no matching draft → continue

4. **Delegate to DRAFT sub-command:**
   - Pass the identified thread and any user-provided reply content to the **draft** sub-command
   - The draft sub-command handles recipient determination, HTML composition, and draft creation as normal
   - All draft sub-command safeguards apply (never send, show recipients, clarify if ambiguous)

### Hard-Block Response Formats

**Already replied:**
```markdown
⛔ **Thread already responded to**
- **Thread:** [Subject]
- **Your reply sent:** [DD MMM YYYY HH:MM SGT]
- **Reply summary:** [≤30-word summary of your sent message]
- **Link:** [📧 Open Thread](https://mail.google.com/mail/u/0/#inbox/MSG_ID)

No draft created. If you'd like to send a follow-up, use the **draft** sub-command directly.
```

**Duplicate draft exists:**
```markdown
⛔ **Draft already exists for this thread**
- **Thread:** [Subject]
- **Existing draft created:** [DD MMM YYYY HH:MM SGT]
- **Draft summary:** [≤30-word summary of draft content]
- **Link:** [📧 Open Draft](https://mail.google.com/mail/u/0/#drafts/DRAFT_MSG_ID)

No new draft created. Review or edit the existing draft in Gmail.
```

### Safeguards

- Inherits all safeguards from the **draft** sub-command
- Both checks (already replied + existing draft) must pass before any draft is created
- If Gmail search fails or returns ambiguous results during either check, ask the user for clarification rather than proceeding

---

## Sub-Command: PROPOSE

**Purpose:** Reply to a meeting request email with a proposed meeting time. If the sender has already suggested a specific time, validate it against your calendar and availability rules. If it works, accept it. If not — or if no time was proposed — find the next available slot and counter-propose. Always saves to draft. Never sends.

**Requires:** A target thread — identified by person name, subject, or topic from the user.

> **Connector:** Follow the native connector policy and capability routing above. Never auto-fallback.

### Steps

1. **Identify the target thread:**
   - Thread already in context → use it
   - User names a person/subject → search Gmail to find thread
   - If multiple matches → ask which one
   - Read the full thread using the host's native full-thread capability

2. **Run safety checks (same as RESPOND):**
   - **Check 1 — Already replied:** If a message from `chris@sentient.io` is newer than the most recent inbound message → hard-block (show existing reply summary and link, do not proceed)
   - **Check 2 — Existing draft:** Search `in:drafts subject:"{thread subject}"` → if found → hard-block (show draft summary and link, do not proceed)

3. **Parse the thread for a proposed time and meeting format:**
   - Scan the most recent inbound message(s) for explicit date/time patterns (e.g. "Monday 3pm", "March 20 at 14:00", "next Tuesday morning")
   - Also check for duration hints (e.g. "30-minute call", "an hour", "quick catch-up")
   - **Detect meeting format** — scan the thread for physical meeting signals:
     - Signals: "meet in person", "your office", "Sentient office", "come to", "drop by", "face to face", "F2F", "in-person", "office visit", "meet at your place"
     - If the sender requests a physical meeting **at the Sentient office specifically** → set `meeting_format = PHYSICAL_SENTIENT`
     - If the sender requests a physical meeting **at a neutral or unspecified location** → set `meeting_format = PHYSICAL_OTHER`
     - If no physical meeting signals → set `meeting_format = ONLINE` (default)
   - **If a specific time is found** → go to Step 4A
   - **If no time is found** → go to Step 4B

4A. **Validate the proposed time (sender proposed a time):**
   - Retrieve calendar events through the `daily-calendars` availability workflow when it is installed; otherwise use the connected native Calendar capability available in the current host
   - If no Calendar capability is available, report that availability cannot be verified and stop before drafting
   - Apply your availability rules in order:
     1. Must be a weekday (Mon–Fri)
     2. Must fall within 10:00 AM – 6:00 PM SGT
     3. Must not overlap the lunch block (12:00 PM – 2:00 PM)
     4. Must not start within 30 minutes of an existing meeting ending
     5. Must not conflict with any existing event
   - **If available** → go to Step 5A (accept)
   - **If unavailable** → go to Step 5B (counter-propose), noting the specific rule that blocked it

4B. **Find the next available slot (no time proposed):**
   - Starting from the next working day (or later today if before 4:00 PM and a slot exists), scan forward day by day
   - For each day, retrieve calendar events and identify open windows respecting all four availability rules
   - Use a default meeting duration of **60 minutes** unless the thread specifies otherwise
   - Take the earliest open slot found → go to Step 5B (propose)

5A. **Draft: Accept their proposed time:**
   - Compose a warm, concise reply confirming the proposed date and time
   - Include the meeting date, time (SGT), and duration if mentioned
   - **Apply meeting format logic:**
     - `PHYSICAL_SENTIENT`: Politely acknowledge the request and note that Sentient operates fully virtually and does not have a physical office. Ask whether they would prefer to meet virtually (Google Meet) or in person — and if in person, invite them to suggest a convenient location
     - `PHYSICAL_OTHER`: Acknowledge the in-person preference; confirm the proposed location if stated, or invite the sender to suggest one
     - `ONLINE` (default): Propose a Google Meet video call; note that an invite with a meeting link will be sent upon confirmation
   - Delegate to DRAFT sub-command for HTML formatting and draft creation

5B. **Draft: Counter-propose or propose a new time:**
   - Compose a reply that:
     - (If counter-proposing) Politely notes the proposed time doesn't work, without disclosing internal meeting details
     - Proposes the specific available date and time (in SGT, with day of week)
     - States the proposed duration (default 60 minutes or as derived from thread)
     - Invites confirmation or an alternative if the slot doesn't suit them
   - **Apply meeting format logic:**
     - `PHYSICAL_SENTIENT`: Politely note that Sentient operates fully virtually and does not have a physical office. Ask whether they would prefer to meet virtually (Google Meet) or in person — and if in person, invite them to suggest a convenient location
     - `PHYSICAL_OTHER`: Acknowledge the in-person preference; confirm or propose the meeting location alongside the proposed time
     - `ONLINE` (default): Propose a Google Meet video call; note that an invite with a meeting link will follow upon confirmation
   - Delegate to DRAFT sub-command for HTML formatting and draft creation

### Availability Rules (mirrors daily-calendars AVAILABLE)

| Rule | Constraint |
|------|-----------|
| Working days | Monday – Friday only |
| Working hours | 10:00 AM – 6:00 PM SGT |
| Lunch block | No meetings 12:00 PM – 2:00 PM |
| Gap between meetings | Minimum 30 minutes after any existing meeting ends |
| Default duration | 60 minutes (override from thread if stated) |

### Hard-Block Response Formats

**Already replied:**
```
⛔ Thread already responded to
- Thread: [Subject]
- Your reply sent: [DD MMM YYYY HH:MM SGT]
- Reply summary: [≤30-word summary]
- Link: [📧 Open Thread]

No draft created. Use the draft sub-command directly if you want to send a follow-up.
```

**Duplicate draft exists:**
```
⛔ Draft already exists for this thread
- Thread: [Subject]
- Existing draft created: [DD MMM YYYY HH:MM SGT]
- Draft summary: [≤30-word summary]
- Link: [📧 Open Draft]

No new draft created. Review or edit the existing draft in Gmail.
```

### Confirmation to User (after draft is created)

```
✅ Meeting reply drafted
- Thread: [Subject]
- Sender: [Name / Email]
- Outcome: [Accepted their proposed time / Counter-proposed new slot / Proposed new slot]
- Proposed time: [Day, DD MMM YYYY, HH:MM – HH:MM SGT]
- Meeting format: [Online (Google Meet) / In-person at [location] / Note: No Sentient office — sender asked to choose format or suggest location]
- Recipients: To: [name] | Cc: [names if any]
- Link: [📧 Open Draft]

Review and send from Gmail when ready.
```

### Safeguards

- **Never send** — always draft only, every time, no exceptions
- **Always show recipients** before creating draft
- **Never disclose** the title or details of conflicting calendar events to the sender
- **If thread contains no meeting request** — inform the user and stop; do not draft a reply
- **Sentient virtual office policy** — Sentient operates fully virtually and has no physical office. If a sender requests a physical meeting at the Sentient office, always communicate this politely, then ask whether they prefer a virtual meeting (Google Meet) or in person at a location of their choosing. Never imply a Sentient office exists
- **If multiple proposed times are found** — use the most recent one
- **If proposed time is ambiguous** (e.g. "sometime next week") — treat as no time proposed and find the next available slot

---
