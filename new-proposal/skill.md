---
name: new-proposal
description: Assemble a customer-ready proposal by pairing the latest customer brief with the selected product's whitepaper and Sentient.io templates. Only the product name is required from the user; the skill automatically loads the supporting assets stored in this directory.
---

# New Proposal Skill

Produce a polished, Sentient.io-branded proposal packet without lengthy intake cycles. Once the user tells you which product the proposal is for, fetch the matching whitepaper from the `proposals/` library, combine it with the AI proposal outline, and generate a structured draft that can be exported immediately.

## When to Use
- A user says "Create a proposal for <Product>" or similar phrasing that clearly identifies the product
- Sales or delivery teams need a proposal derived from existing whitepapers and the customer brief skill output
- Rapid follow-ups are required after discovery sessions and there is no time for manual document assembly

## Required User Input
- **Product name only.** Treat the first explicit product reference as canonical. Do not request any other mandatory inputs. Any missing deal details should remain as clearly labeled placeholders in the output.

## Automatic Data Sources
1. **Product Whitepapers** – Located in `proposals/`. File names use the pattern `<Product Name>.md`. Load the file matching the requested product. If multiple candidates exist, select the closest match and note the assumption.
2. **Proposal Outline Template** – `templates/proposal-outline.md` provides the section scaffolding and formatting guidance.
3. **Brand Voice** – Reference `../sentient-brand-guideline/skill.md` as needed to maintain tone, typography, and styling guidance.
4. **Customer Brief Context (Optional)** – If a recent brief exists (for example, outputs from the `customer-brief` skill stored in the workspace), ingest it automatically. When unavailable, leave TODO placeholders for customer-specific facts rather than prompting the user.

## Workflow

### 1. Confirm Product & Load Assets
1. Restate the requested product to show understanding.
2. Locate `proposals/<Product>.md`. If not found, list available filenames from the folder and ask the user to choose one of them (this is the only follow-up question permitted).
3. Load `templates/proposal-outline.md` to understand the expected structure.
4. Optionally open the Sentient brand guideline skill to ensure language stays on-brand.

### 2. Extract Product Intelligence
1. Parse the whitepaper for:
   - Positioning statements and differentiators
   - Capability pillars / feature sets
   - Proof points (metrics, case studies, testimonials)
   - Implementation models and security/governance claims
2. Capture these into reusable bullet banks for later sections (Solution, Value, Appendix).

### 3. Incorporate Customer Insight
1. Automatically ingest the latest customer brief if one is available. Prioritize executive summary, pain points, stakeholders, success metrics, and timeline signals.
2. Map each high-priority customer need to a relevant capability from the whitepaper.
3. When customer data is missing, insert a placeholder such as `{{Insert customer goals here}}` and note it in the QA checklist instead of interrogating the user.

### 4. Draft the Proposal
Follow the outline from `templates/proposal-outline.md`:
1. **Cover Page Metadata** – Proposal title, product name, customer name placeholder, date stamp (`<YYYYMMDD>`), and revision counter `R1`.
2. **Executive Overview** – 2–3 paragraphs linking customer goals to headline product value.
3. **Proposed Solution** – Structure into subsections (Architecture, Deployment Approach, Key Modules). Tie every claim back to whitepaper language or brief insights.
4. **Value & ROI Justification** – Blend quantitative metrics from the whitepaper with customer pain points. Use tables when multiple KPIs exist.
5. **Pricing Placeholder** – Render a clearly labeled section instructing account teams to insert pricing (do **not** fabricate numbers).
6. **Implementation Plan** – Provide a phased roadmap (e.g., Discovery → Enablement → Launch → Optimization) with responsibilities and success criteria.
7. **Next Steps & Call to Action** – Outline approvals, follow-up meetings, and sign-off process.
8. **Appendix** – Include security posture, compliance credentials, integration catalogue, and any cited case studies.

### 5. Output & Packaging
1. Present the full proposal in Markdown, using heading levels defined in the template.
2. Preserve placeholder tokens in double braces so they are easy to search and replace (`{{Customer Name}}`, `{{Decision Date}}`).
3. Offer optional export guidance: how to convert the markdown into PDF/DOCX or adapt the included `Sentient.io Proposal to WeCom (2025-05-14).docx` template.
4. Summarize key highlights and remaining TODOs at the top of the chat response so account teams can act immediately.

## Quality Checklist
Before finalizing the response, verify:
- [ ] Only the product name was requested from the user (aside from resolving ambiguous file matches).
- [ ] The correct whitepaper from `proposals/` was used and cited within the draft where relevant.
- [ ] All placeholders are clearly labeled with `{{ }}` and accompanied by instructions if critical.
- [ ] Executive Overview, Solution, Value, Implementation, Pricing Placeholder, Next Steps, and Appendix are all populated.
- [ ] Tone aligns with Sentient.io brand guidance (confident, consultative, enterprise-ready).
- [ ] Summary section surfaces 3–5 deal-critical talking points plus outstanding actions.

## Error Handling
- If no matching whitepaper exists, provide the list of available options and pause until the user picks one.
- When supporting assets fail to load, continue with the information available and flag the missing reference explicitly.
- If customer brief content cannot be located, state this in the summary and keep placeholders instead of fabricating details.

## Packaging Notes
- Store this file at `new-proposal/skill.md`.
- Keep whitepapers inside `new-proposal/proposals/` so the skill can load them automatically based solely on the product name.
- Maintain proposal templates in `new-proposal/templates/` for consistent formatting across exports.
