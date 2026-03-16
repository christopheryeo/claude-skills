---
name: daily-knowledge
description: >
  Personal knowledge management skill for Christopher Yeo with three sub-commands. FIND: search Christopher's Personal - Daily Reading folder in Google Drive first, fetch full document content, then fall back to web search only if nothing is found — ensuring his curated knowledge is always the first source consulted. CLASSIFY: given a piece of new knowledge, read the Knowledge Fabric and determine where in the AI Workforce structure it belongs — which section, which file, and which team member owns that domain. FILE: write classified knowledge to its target destination after Christopher confirms. CLASSIFY must always be run before FILE. Use this skill whenever Christopher asks to find, search, look up, or get a briefing on any topic; whenever he provides new knowledge and wants it stored; whenever he asks "where does this go?", "file this", "add this to the knowledge base", "classify this", or any knowledge retrieval, classification, or filing request.
---

# Daily Knowledge Skill

## Purpose

This skill manages the flow of knowledge into and out of Christopher's Knowledge Fabric — the structured system that underpins the entire Sentient AI Workforce. It has three operations: retrieving knowledge (FIND), routing knowledge to the right place (CLASSIFY), and writing knowledge to that place (FILE).

The Knowledge Fabric rests on **three essential knowledge layers:**

1. **Long Term Memory** — Durable reference knowledge stored in shared Google Drive files (profiles, company data, stakeholder records). Consulted on demand.
2. **Operational Knowledge** — Domain-specific files in each AI Workforce member's `Knowledge/` sub-folder. The working files that power day-to-day execution.
3. **Learned Preferences** — Ever-present knowledge embedded in the `## Learned Preferences` section of each `claude.md` file. Always loaded, always applied — no lookup required.

Every CLASSIFY and FILE operation routes knowledge to one of these three layers.

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

## CLASSIFY Sub-command

**Trigger:** Christopher provides new knowledge and asks where it should go, says "classify this", or provides information that needs to be routed to the right place in the Knowledge Fabric.

CLASSIFY is read-only — it analyses and recommends a destination but does not write anything.

### Step 1 — Read the Knowledge Fabric

Read `Knowledge/knowledge_fabric.md` to load the full structure. The fabric's three knowledge layers each contain classifiable destinations. When routing new knowledge, first determine which layer it belongs to, then identify the specific target file within that layer.

---

#### Layer 1: Long Term Memory

Durable reference knowledge in the root `Knowledge/` folder — company-wide files that any agent can read. These are consulted on demand and change infrequently.

| File | Content type |
|---|---|
| `chris-profile.md` | Biographical, contact, career, education, personality details about Christopher |
| `company-profile.md` | Sentient.io company facts: products, markets, customers, revenue, funding, strategy, IPO |
| `Shareholder_Contacts.md` | Shareholder names and email addresses |
| `schedule.md` | Scheduled task definitions (ID, cron, prompt, enabled status) |
| `Onboarding.md` | AI Workforce governance rules and folder standards |
| `personal-drives.md` | Descriptions of Christopher's three personal Google Drive folders |
| `knowledge_fabric.md` | The fabric index itself — new sections, files, or sources |

Also includes **Protocols & Procedures** within the fabric:
- Meeting Minutes lookup sequence
- Lead-to-Prospect Handoff (Mary → Donny)
- Any new operational protocols or standard procedures

---

#### Layer 2: Operational Knowledge

Domain-specific files in each AI Workforce member's `Knowledge/` sub-folder. These are the working files that power day-to-day execution — the most precise filing targets. Always check whether new knowledge fits an existing operational file before defaulting to the broader domain folder.

**Domain owners (for routing when no specific operational file exists):**

| Domain | Owner | Examples of what belongs here |
|---|---|---|
| **Finance** | Eddie (CFO) | Financial data, bank info, investments, grants, legal/loans, payroll |
| **Sales** | Donny (Sales) | Pipeline updates, accounts, tenders, partnerships, alliances |
| **Marketing** | Mary (Marketing) | Brand guidelines, leads, collateral, investor materials, product info |
| **Projects** | Cedric (Projects) | Stakeholder reports, project updates, R&D, technical deliverables |
| **Dev** | Alex (Dev) | Tech stack, skills, code repos, development references |
| **Admin/HR** | Vivien (PA) | HR records, admin docs, legal templates, ACRA/BizFile, expense claims |
| **CEO Ops** | Christopher (root) | Daily plans, journals, learning materials |

**Specific operational files (preferred targets):**

| Member | File / Folder | Content type |
|---|---|---|
| **Eddie (CFO)** | `Eddie (CFO)/Knowledge/Shareholder_Contacts.md` | Eddie's working copy of shareholder contacts (must sync with root copy) |
| **Eddie (CFO)** | `Eddie (CFO)/Knowledge/Creditor_Interactions_Tracker.md` | Creditor communications, payment arrangements, outstanding obligations |
| **Eddie (CFO)** | `Eddie (CFO)/Knowledge/Legal & Loans/` | Loan agreements and legal settlement documents |
| **Eddie (CFO)** | `Eddie (CFO)/Knowledge/Payroll/` | Monthly payroll records — pay-run screenshots and salary reports |
| **Eddie (CFO)** | `Eddie (CFO)/Knowledge/Reference/` | CFO research and compliance material (skills research, compliance tracker) |
| **Mary (Marketing)** | `Mary (Marketing)/Knowledge/Carbon Amber Brand Guidelines.md` | Carbon Amber brand identity — colours, typography, tone, logo usage |
| **Mary (Marketing)** | `Mary (Marketing)/Knowledge/Marketing Materials Index.md` | Master index of all marketing collateral with locations and versions |
| **Mary (Marketing)** | `Mary (Marketing)/Knowledge/Lead Generation Log.md` | Inbound/outbound lead log with source, status, and follow-up actions |
| **Mary (Marketing)** | `Mary (Marketing)/Knowledge/Sentient Ecosystem.csv` | Partner and product ecosystem map |
| **Cedric (Projects)** | `Cedric (Projects)/Knowledge/` | Stakeholder monitoring reports — engagement, sentiment, actions |
| **Alex (Dev)** | `Alex (Dev)/Knowledge/techstack.md` | Technology stack reference — languages, frameworks, infrastructure |
| **Alex (Dev)** | `Alex (Dev)/Knowledge/Skills_Comparison.md` | Claude Skills comparison matrix — capabilities and benchmarks |
| **Vivien (PA)** | `Vivien (PA)/Knowledge/` | (Empty — reserved for admin procedures, HR policies, legal references) |
| **Donny (Sales)** | `Donny (Sales)/Knowledge/Sales Prospects Tracker.md` | Active sales pipeline from handoff to close |

---

#### Layer 3: Learned Preferences (Ever-Present Knowledge)

Knowledge embedded in the `## Learned Preferences` section of `claude.md` files. Unlike the other two layers, Learned Preferences are always loaded and always applied — they don't need to be looked up. This makes them the right destination for recurring patterns, terminology, corrections, workflow preferences, and decision-making styles that should influence every session.

| Scope | Target file | What belongs here |
|---|---|---|
| Cross-functional / CEO-level | `claude.md` (root) | Christopher's global preferences, protocols, correction dictionaries, and patterns that apply across all domains |
| Finance-specific | `Eddie (CFO)/claude.md` | How Christopher wants financial reports, how Eddie should handle creditor queries, etc. |
| Sales-specific | `Donny (Sales)/claude.md` | Sales process preferences, proposal formatting, pipeline reporting style |
| Marketing-specific | `Mary (Marketing)/claude.md` | Brand tone preferences, lead handling rules, content formatting |
| Projects-specific | `Cedric (Projects)/claude.md` | Stakeholder reporting preferences, project update formats |
| Dev-specific | `Alex (Dev)/claude.md` | Technical preferences, code review standards, skill development patterns |
| Admin/HR-specific | `Vivien (PA)/claude.md` | Admin workflow preferences, document handling, scheduling patterns |

**When to route to Learned Preferences instead of the other layers:**
- The knowledge is about *how* Christopher wants something done, not *what* the facts are → Layer 3
- It's a correction, abbreviation, or terminology mapping that should be applied automatically → Layer 3
- It's a process or workflow that Christopher expects to be followed without reminding → Layer 3
- It's a factual record (profile data, company info, contacts) → Layer 1
- It's a working document that gets updated as part of operations → Layer 2

### Step 2 — Analyse the Input

Determine what the new knowledge is about:
- **Which layer?** — Is it a durable fact (Layer 1: Long Term Memory), a working operational file (Layer 2: Operational Knowledge), or a preference/pattern/correction (Layer 3: Learned Preferences)?
- **Subject matter** — What domain does it cover? (finance, sales, HR, personal, governance, etc.)
- **Knowledge type** — Is it a fact, a preference, a process, a contact, a reference, a new source?
- **Scope** — Does it apply to one AI Workforce member's domain, or is it cross-functional?
- **Sensitivity** — Is it personal/private (→ personal drives or root claude.md) or operational (→ shared Knowledge files)?

### Step 3 — Return Classification

Present the classification to Christopher as a clear recommendation:

```
Classification:
- Layer: [1: Long Term Memory / 2: Operational Knowledge / 3: Learned Preferences]
- Target file: [exact file path]
- Owner: [AI Workforce member name and role]
- Action: [append to existing section / create new entry / add new section]
- Rationale: [one sentence explaining why this is the right destination and layer]
```

If the classification is ambiguous (could belong in multiple places), present the top 2 options and ask Christopher to choose.

If the knowledge doesn't fit any existing section, recommend creating a new entry in the knowledge fabric and suggest where it should sit in the structure.

**CLASSIFY never writes. It only recommends.**

---

## FILE Sub-command

**Trigger:** Christopher says "file this", "go ahead and file it", "add it", or confirms a CLASSIFY recommendation.

FILE is the write operation. It requires either a preceding CLASSIFY recommendation that Christopher has confirmed, or an explicit destination from Christopher.

### Pre-condition

FILE must not execute without one of:
1. A CLASSIFY recommendation that Christopher has explicitly confirmed (e.g., "yes, file it there")
2. An explicit destination from Christopher (e.g., "add this to company-profile.md")

If neither exists, run CLASSIFY first and ask for confirmation.

### Step 1 — Read the Target File

Read the target file to understand its current structure, formatting, and where the new content should be inserted.

### Step 2 — Write the Knowledge

- **Appending to an existing file:** Match the existing formatting, heading structure, and tone. Insert in the most logical location (chronologically, alphabetically, or by section relevance).
- **Adding to Learned Preferences:** Append under the `## Learned Preferences` heading with a clear, descriptive sub-heading.
- **Creating a new file:** Follow the conventions established in `Onboarding.md` for file naming and structure.

### Step 3 — Update the Knowledge Fabric Index

If the filing action created a new file, a new section, or a new knowledge source:
- Read `Knowledge/knowledge_fabric.md`
- Add the appropriate entry to the Folder Directory table and/or the relevant section
- Update the `Last Updated` date

If the action was an append to an existing file, no fabric update is needed.

### Step 4 — Confirm to Christopher

Report what was written, where, and confirm the fabric index was updated if applicable. Keep it to one or two sentences.

---

## Key Implementation Notes

1. **Always search Drive first in FIND** — never go straight to web search, even if the topic seems obscure
2. **Always fetch after search in FIND** — the search step alone is not enough for large files; fetch is required
3. **`document_ids` must be an array** — passing a plain string will throw a "Field required" error
4. **CLASSIFY before FILE — always** — never write knowledge without classification and confirmation
5. **Confirm before writing** — FILE never executes without Christopher's explicit go-ahead
6. **Apply transcription corrections** — per Christopher's preferences: "Jack" → "Jeg", "VCOM" → "WeCom", "DSDA" → "DSTA"
7. **Update the fabric when structure changes** — any new file or section added via FILE must be reflected in `knowledge_fabric.md`
