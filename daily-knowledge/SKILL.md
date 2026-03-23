---
name: daily-knowledge
description: >
  Personal knowledge management skill with three primary sub-commands plus one informational query. FIND: search Daily Reading in Google Drive first, fetch full content, fall back to web search if nothing found. FILE: classify knowledge against the Knowledge Fabric, present recommendation for confirmation, then write to the destination using the fabric's filing instructions. LEARN: extract significant learnings from the conversation, write to Learnings journal, and auto-classify each for potential filing. CLASSIFY: lightweight read-only lookup for "where does this go?" questions — does not write. Use whenever Christopher asks to find, search, look up, or brief on any topic; provides new knowledge to store; says "where does this go?", "classify this", "file this", "what did we learn", "capture learnings", "log what we learned", or "learn".
---

# Daily Knowledge Skill

## Purpose

This skill manages the flow of knowledge into and out of Christopher's Knowledge Fabric — the structured system that underpins the entire Sentient AI Workforce. It has three primary operations: retrieving knowledge (FIND), writing knowledge to the right place (FILE), and extracting learnings from conversation (LEARN). A fourth operation (CLASSIFY) exists as a lightweight informational query for when Christopher wants to know where something belongs without filing it.

The Knowledge Fabric (`Knowledge/knowledge_fabric.md`) is the single source of truth for both **where** knowledge belongs and **how** to write it there. Every destination in the fabric includes inline filing instructions (storage type, write method, format, constraints). FILE reads these instructions before writing.

The Knowledge Fabric rests on **three essential knowledge layers:**

1. **Long Term Memory** — Durable reference knowledge stored in shared Google Drive files (profiles, company data, stakeholder records). Consulted on demand.
2. **Operational Knowledge** — Domain-specific files in each AI Workforce member's `Knowledge/` sub-folder. The working files that power day-to-day execution.
3. **Learned Preferences** — Ever-present knowledge embedded in the `## Learned Preferences` section of each `claude.md` file. Always loaded, always applied — no lookup required.

---

## FIND Sub-command

**Trigger:** Christopher asks to find, search, look up, or get a briefing on any topic.

Execute this three-step sequence:

### Step 1 — Search Personal - Daily Reading

Use `google_drive_search` to search Christopher's curated news archive.

- **Folder ID:** `1ULQ-wkf6DEXjuA38xPtFHVWe6NrsAHRo`
- **Query format:**
  ```
  '1ULQ-wkf6DEXjuA38xPtFHVWe6NrsAHRo' in parents and fullText contains '<topic>'
  ```
- Set `order_by` to `relevance desc`
- Request up to 10 results

The search returns metadata and, for small files, inline content. Large files (4MB+) return a size error — this is expected and resolved in Step 2.

### Step 2 — Fetch Full Content

Use `google_drive_fetch` to retrieve the full content of matching documents.

**Critical — the fetch tool requires `document_ids` as a JSON array of strings, never a plain string:**

```json
{ "document_ids": ["doc_id_1", "doc_id_2", "doc_id_3"] }
```

- Fetch up to **3 most recently dated** documents (named `YYYY-MM-DD Articles`)
- Strip the `drive:///` prefix from URIs — use only the alphanumeric ID
- Extract all content relevant to the topic

### Step 3 — Synthesise or Fall Back

**If relevant content found in Drive:**
- Synthesise an executive briefing from the fetched documents
- Note article dates so Christopher knows how recent the information is
- Do not go to the web unless Christopher asks for more current data

**If no relevant content found in Drive:**
- Tell Christopher explicitly: "Nothing found in your Daily Reading archive on this topic."
- Fall back to `WebSearch` with a well-formed query
- Synthesise live results

### FIND Output Format

Present as a concise executive briefing: lead with the key insight, group by theme or date, note the source for each point (Drive article title + date, or web URL), and close with a "Sources:" section. Keep it direct and action-oriented.

---

## FILE Sub-command

**Trigger:** Christopher says "file this", "go ahead and file it", "add it", or provides new knowledge with a clear intent to store it.

FILE is the primary write operation. It is **self-sufficient** — it classifies, confirms, and writes in a single flow. There is no need to run CLASSIFY first.

### Step 0 — Classify (internal)

Read `Knowledge/knowledge_fabric.md` to determine where the knowledge belongs and how to write it there.

**Determine the destination:**
- **Which layer?** — Is it a durable fact (Layer 1: Long Term Memory), a working operational file (Layer 2: Operational Knowledge), or a preference/pattern/correction (Layer 3: Learned Preferences)?
- **Subject matter** — What domain does it cover? (finance, sales, HR, personal, governance, etc.)
- **Knowledge type** — Is it a fact, a preference, a process, a contact, a reference, a new source?
- **Scope** — Does it apply to one AI Workforce member's domain, or is it cross-functional?
- **Sensitivity** — Is it personal/private (→ personal drives or root claude.md) or operational (→ shared Knowledge files)?

**Routing rules (when to use which layer):**
- The knowledge is about *how* Christopher wants something done, not *what* the facts are → Layer 3 (Learned Preferences)
- It's a correction, abbreviation, or terminology mapping that should be applied automatically → Layer 3
- It's a process or workflow that Christopher expects to be followed without reminding → Layer 3
- It's a factual record (profile data, company info, contacts) → Layer 1 (Long Term Memory)
- It's a working document that gets updated as part of operations → Layer 2 (Operational Knowledge)

Always check whether new knowledge fits an existing operational file before defaulting to the broader domain folder.

**Read the filing instructions** for the identified destination from the fabric. Each destination includes inline instructions covering: storage type (local markdown or Google Drive), write method (Edit tool, Google Docs API, etc.), format template, and constraints.

If the classification is ambiguous (could belong in multiple places), present the top 2 options and ask Christopher to choose.

### Step 1 — Present Recommendation and Confirm

Present the classification to Christopher:

```
Filing recommendation:
- Layer: [1: Long Term Memory / 2: Operational Knowledge / 3: Learned Preferences]
- Target file: [exact file path]
- Owner: [AI Workforce member name and role]
- Write method: [from fabric filing instructions]
- Action: [append to existing section / create new entry / add new section]
- Rationale: [one sentence explaining why this is the right destination]
```

**Wait for Christopher's explicit confirmation before writing.** FILE never writes without approval. If Christopher redirects to a different destination, update the classification and proceed.

### Step 2 — Read the Target File

Read the target file to understand its current structure, formatting, and where the new content should be inserted.

### Step 3 — Write the Knowledge

Follow the filing instructions from the fabric for this destination:

- **Storage type:** Use the Edit tool for local markdown files (Dropbox). Use the appropriate Google Docs/Drive API tool for Google Drive documents.
- **Write method:** Follow the specific method (append to bottom, add table row, insert into section, etc.) as documented in the fabric.
- **Format:** Match the existing formatting, heading structure, and tone of the target file. If the fabric specifies a format template, use it.
- **Constraints:** Respect all constraints (sync requirements, read-only flags, confirmation gates, tab limitations, append-only rules, etc.).

**Specific patterns:**
- **Appending to an existing file:** Match the existing formatting. Insert in the most logical location (chronologically, alphabetically, or by section relevance).
- **Adding to Learned Preferences:** Append under the `## Learned Preferences` heading with a bold sub-heading (`### [Descriptive Title]`) followed by concise, actionable text.
- **Creating a new file:** Follow the conventions established in `Onboarding.md` for file naming and structure.
- **Google Drive documents:** Use `google_docs_append_text_to_document` for append-only targets. Respect tab limitations (first/default tab only where noted).

### Step 4 — Update the Knowledge Fabric Index

If the filing action created a new file, a new section, or a new knowledge source:
- Read `Knowledge/knowledge_fabric.md`
- Add the appropriate entry to the Folder Directory table and/or the relevant section
- Include filing instructions for the new destination
- Update the `Last Updated` date

If the action was an append to an existing file, no fabric update is needed.

### Step 5 — Confirm to Christopher

Report what was written, where, and confirm the fabric index was updated if applicable. Keep it to one or two sentences.

---

## CLASSIFY Sub-command (Informational Query)

**Trigger:** Christopher asks "where does this go?", "classify this", or wants to know where knowledge belongs without actually filing it.

CLASSIFY is a **read-only informational query** — it analyses and recommends a destination but does not write anything. It is not a required pre-step for FILE; FILE handles classification internally.

Use CLASSIFY when Christopher wants to understand the fabric routing without committing to a write operation.

### Steps

1. **Read the Knowledge Fabric.** Read `Knowledge/knowledge_fabric.md` to load the full structure.

2. **Analyse the input.** Determine which layer, domain, knowledge type, scope, and sensitivity apply (same logic as FILE Step 0).

3. **Return classification.** Present the recommendation:

```
Classification:
- Layer: [1: Long Term Memory / 2: Operational Knowledge / 3: Learned Preferences]
- Target file: [exact file path]
- Owner: [AI Workforce member name and role]
- Write method: [from fabric filing instructions]
- Action: [append to existing section / create new entry / add new section]
- Rationale: [one sentence explaining why this is the right destination and layer]
```

If the classification is ambiguous (could belong in multiple places), present the top 2 options and ask Christopher to choose.

**CLASSIFY never writes. It only recommends.** If Christopher then says "file it", proceed to FILE Step 1 (confirmation) using the classification already determined.

---

## LEARN Sub-command

**Trigger:** Christopher says "what did we learn", "capture learnings", "log what we learned", "learn", or asks to extract insights from the current conversation.

LEARN is a compound operation — it extracts, classifies, and journals in a single flow. It reviews the preceding conversation, identifies significant learnings, classifies each one against the Knowledge Fabric, writes them to the Learnings journal (after checking for duplicates), and presents filing recommendations.

### What Qualifies as a "Significant Learning"

Not every piece of conversation is a learning. LEARN should extract only items that meet at least one of these criteria:

- **Structural insight** — A gap, inconsistency, or improvement opportunity discovered in the Knowledge Fabric, folder structure, or AI Workforce setup
- **Behavioural observation** — A pattern, quirk, or limitation discovered in a tool, skill, API, or system during use
- **Process improvement** — A better way of doing something that emerged from the work (a new protocol, a shortcut, a validation technique)
- **Domain knowledge** — A new fact, relationship, or context about the business, a stakeholder, a product, or a market that was surfaced during the conversation
- **Decision or rationale** — A significant decision Christopher made during the session, along with the reasoning, that should be remembered

Do **not** extract: routine task completions, trivial observations, status updates, or anything already captured in the plans/audit files.

### Step 1 — Review the Conversation

Scan the full conversation history from the current session. Identify all candidate learnings that meet the criteria above. Aim for quality over quantity — 2–5 learnings per session is typical. A session with no significant learnings is also valid; report "No significant learnings identified in this session" and stop.

### Step 2 — Draft the Learnings

For each learning, write a concise entry in this format:

```markdown
- **[Short descriptive title].** [One to three sentences explaining the learning — what was discovered, why it matters, and any implication for future work.]
```

Proceed directly — do not pause for Christopher's approval on drafted entries.

### Step 3 — Auto-Classify Each Learning

For each drafted learning, run the classification logic (same as FILE Step 0) to determine where it should also be filed in the Knowledge Fabric. Read `Knowledge/knowledge_fabric.md` for destinations and filing instructions.

Present all classifications together in a summary table:

```
| # | Learning | Layer | Target file | Owner | Action |
|---|----------|-------|-------------|-------|--------|
| 1 | [title]  | [1/2/3] | [path]    | [name] | [append/create] |
| 2 | [title]  | [1/2/3] | [path]    | [name] | [append/create] |
```

If a learning is purely observational and does not need to be filed anywhere beyond the journal (e.g., a validated finding with no action), mark it as `Journal only` in the Action column.

### Step 4 — Write to the Learnings Journal

1. **Locate the journal.** Look for `Journals/YYYY-MM Learnings.md` where `YYYY-MM` is the current month. If it does not exist, create it with the heading `# YYYY-MM Learnings`.
2. **Find or create the date header.** Look for `## YYYY-MM-DD` matching today's date. If it exists, read all existing entries under that date. If not, insert a new date header in reverse-chronological position (newest first).
3. **Check for duplicates.** Before writing each learning, compare it against all existing entries in the journal (not just today's date — check the entire file). A learning is a duplicate if an existing entry covers the same core insight, even if the wording differs. Skip any learning that is a duplicate and note it in the output (e.g., "Skipped — duplicate of entry on YYYY-MM-DD").
4. **Write non-duplicate learnings** as bullet points beneath the date header, using the format from Step 2.

### Step 5 — Await Filing Instructions

LEARN does **not** auto-file to the Knowledge Fabric. After presenting the classifications, wait for Christopher to decide:

- **"File all"** — Run FILE (starting from Step 1, since classification is already done) for every classified learning
- **"File 1 and 3"** — Run FILE for specific items only
- **"Just the journal is fine"** — Stop; the journal entries are sufficient
- **"File X as a task instead"** — Add the item to today's daily plan via the daily-plans skill (NEW operation) rather than filing it as knowledge

LEARN never writes to the Knowledge Fabric without explicit confirmation.

### Step 6 — Tag Filed Entries

After FILE successfully writes a learning to the Knowledge Fabric, return to the Learnings journal and append `[FILED]` to the end of that entry's first line (the bold title line). This provides a clear audit trail of which learnings were filed vs journal-only.

**Before filing:**
```markdown
- **Google Docs tab write limitations.** Writes go to the first/default tab only...
```

**After filing:**
```markdown
- **Google Docs tab write limitations.** [FILED] Writes go to the first/default tab only...
```

Only tag entries that were successfully filed. Entries marked `Journal only` or not selected for filing remain untagged.

---

## Key Implementation Notes

1. **Always search Drive first in FIND** — never go straight to web search, even if the topic seems obscure
2. **Always fetch after search in FIND** — the search step alone is not enough for large files; fetch is required
3. **`document_ids` must be an array** — passing a plain string will throw a "Field required" error
4. **FILE is self-sufficient** — it classifies, confirms, and writes in a single flow. CLASSIFY is not a required pre-step.
5. **FILE reads the fabric for both WHERE and HOW** — `Knowledge/knowledge_fabric.md` contains inline filing instructions for every destination. Always read these before writing.
6. **Confirm before writing** — FILE never executes without Christopher's explicit go-ahead
7. **Apply transcription corrections** — per Christopher's preferences: "Jack" → "Jeg", "VCOM" → "WeCom", "DSDA" → "DSTA"
8. **Update the fabric when structure changes** — any new file or section added via FILE must be reflected in `knowledge_fabric.md`, including filing instructions for the new destination
9. **LEARN extracts, not summarises** — learnings should be specific insights, not a summary of the conversation
10. **LEARN classifies first, journals second** — classification happens before journalling so that duplicates can be checked and skipped before writing; the journal is still the guaranteed output, but only for non-duplicate learnings
11. **LEARN can trigger FILE or NEW (daily-plans)** — Christopher may choose to file a learning into the Knowledge Fabric or convert it into a task; support both paths
