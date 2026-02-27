---
name: draft-email
description: >
  Draft a reply email to an existing Gmail thread and save it to the user's drafts folder for approval.
  Use this skill whenever the user asks to "draft a reply", "draft an email response", "write a reply to that email",
  "prepare a response to [person]", "draft something back to [person]", or any similar request to compose a reply
  to an email thread. Also trigger when the user says "reply to Hayden", "respond to that thread", "write back to them",
  or refers to drafting/composing email responses in any way. This skill handles reply-all HTML drafts with quoted
  thread history, saved to Gmail drafts for human review before sending.
---

# Draft Email Reply

This skill drafts a reply-all email to an existing Gmail thread, formats it as HTML, and saves it to the user's Gmail drafts folder for approval. Nothing is sent — the draft sits in Gmail until the user reviews and sends it manually.

## Why this skill exists

Christopher (the user) often needs to reply to email threads after reviewing them with his AI workforce. Rather than switching to Gmail, composing manually, and reformatting, this skill lets him say something like "draft a reply to Hayden saying we'll pay next week" and get a polished, correctly-addressed HTML draft ready for one-click sending.

## How it works

### Step 1: Identify the thread

Figure out which thread the user wants to reply to. There are a few ways this might come up:

- **Thread already in context** — If the conversation already contains a thread that was just read or summarised (e.g., the user said "read that email from Hayden" and now says "draft a reply"), use that thread. You already have the thread ID, participants, and content.
- **User names a person or subject** — Search Gmail to find the relevant thread. Use `gmail_search_messages` with appropriate queries (e.g., `from:hayden.foo@mile.cloud` or `subject:overdue payment`). If multiple threads match, ask the user which one.
- **User provides a thread ID directly** — Rare, but if they do, use it.

Once you have the thread ID, read the full thread using `gmail_read_thread` to get all participants and the message history.

### Step 2: Determine the reply content

The user can work in two modes — ask them if it's not clear from context:

**Mode A — User provides the message:** The user tells you what to say (e.g., "tell him we'll pay $10k by Friday"). Take their intent and compose a professional email in Christopher's voice.

**Mode B — Auto-generate:** The user wants you to propose a reply based on the thread context (e.g., "draft a response to that"). Read the thread carefully, understand what's being asked or discussed, and compose an appropriate reply. Present a brief summary of what you plan to say before creating the draft, so the user can adjust.

### Step 3: Compose the HTML email

Write the reply body in clean, professional HTML. Christopher's communication style is:

- **Professional and warm** — respectful, never cold or overly formal
- **Direct and action-oriented** — gets to the point, states what will happen and when
- **Concise** — no filler, no unnecessary pleasantries beyond a brief greeting
- **Structured when needed** — uses short paragraphs; bullet points only if listing multiple items

HTML formatting guidelines:

- Use `<p>` tags for paragraphs with `style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;"`
- **CRITICAL: Do NOT wrap the body in `<html>`, `<body>`, or `<head>` tags.** Start directly with the first `<p>` tag. Gmail's API handles the outer HTML wrapper — adding these tags causes the raw HTML to display as literal text in the draft instead of being rendered.
- Keep it simple — no fancy layouts, no images, no heavy styling
- Use `<br/>` (self-closing) for line breaks, not `<br>`
- Include a sign-off block: "Best regards," followed by "Christopher Yeo" on the next line (use `<br/>` between them inside a single `<p>` tag)
- Do NOT include a title/role line (no "CEO", "Acting CFO", "Sentient.io") — Christopher's Gmail signature handles that automatically
- Do NOT include contact details (phone, email) in the sign-off — the Gmail signature appends these

Example structure:

```html
<p style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;">Hi Hayden,</p>

<p style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;">Thank you for your patience on this. We will be making the payment of $10,000 by this Friday, 28 February.</p>

<p style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;">I will send the remittance advice once the transfer is complete.</p>

<p style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 14px; color: #333333;">Best regards,<br/>Christopher Yeo</p>
```

### Step 4: Determine recipients (Reply-All)

From the thread, extract all participants for a reply-all:

- **To:** The sender of the most recent message in the thread (the person being replied to)
- **Cc:** All other participants from the thread (from To, Cc fields of recent messages), excluding:
  - Christopher's own email (`chris@sentient.io`)
  - Any duplicate addresses
  - Any automated/noreply addresses (e.g., `cm-service@mile.cloud`, `noreply@...`)

If the most recent message was sent BY Christopher, reply to the recipients of that message instead (i.e., maintain the same addressing).

### Step 5: Create the draft

Use the `gmail_create_draft_reply` MCP tool to create the draft:

- Set the `thread_id` to the thread being replied to
- Set `to` with the primary recipient
- Set `cc` with all other participants
- Set `body` with the HTML content (bare `<p>` tags — no `<html>/<body>` wrapper)
- **Set `body_type` to `html`** — this is critical. Without it, Gmail treats the HTML as plain text and the tags appear as literal characters in the draft.

After creating the draft, confirm to the user:
- Who the draft is addressed to (To and Cc)
- A brief summary of the reply content
- That it's saved in their Gmail drafts folder
- Remind them to review and send from Gmail when ready

### Important safeguards

- **Never send the email.** Always create a draft. The user must review and send manually from Gmail.
- **Always show the user who the email will go to** before creating the draft, especially if there are many Cc recipients.
- **If the user's intent is ambiguous**, ask for clarification rather than guessing. A wrong reply is worse than a small delay.
- **If the thread is very long or complex**, summarise the key context you're basing the reply on so the user can verify you understood correctly.

## Examples

**Example 1 — User provides content:**
> User: "Draft a reply to Hayden saying we'll make the payment by end of this week and I'll send the remittance slip"
>
> Action: Compose HTML reply in Christopher's voice, reply-all to thread participants, save as draft.

**Example 2 — Auto-generate:**
> User: "Draft a response to that Margin Wheeler accounting queries thread"
>
> Action: Read thread, understand the queries, propose a reply that acknowledges and addresses them. Present summary to user first, then create draft on confirmation.

**Example 3 — Thread already in context:**
> User: [just finished reading a thread] "Ok draft a reply"
>
> Action: Ask the user what they'd like to say, or offer to auto-generate based on the thread context.
