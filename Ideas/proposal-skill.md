# Proposal Skill Idea

## Mission
Enable account teams to rapidly assemble a polished sales proposal that aligns customer-specific pain points from briefs with product capabilities documented in the whitepaper. The skill should ingest the latest customer brief alongside the product whitepaper to generate a structured proposal draft that can be sent directly to the prospect.

## Why It Matters
- Reduces turnaround time between discovery calls and proposal delivery.
- Ensures proposals stay consistent with the product messaging, positioning, and differentiators outlined in the whitepaper.
- Tailors value narratives and solution components to the unique needs captured in each customer brief, increasing conversion likelihood.

## Primary Triggers
- "Draft a proposal for [Customer] based on their brief."
- "Turn the latest [Customer] brief into a proposal."
- "Prepare a proposal combining the product whitepaper and [Customer] insights."

## Inputs & Data Sources
1. **Customer Brief Skill Output**: Required to understand account context, pain points, stakeholders, timelines, and desired outcomes.
2. **Product Whitepaper**: Canonical reference for product capabilities, technical architecture, security posture, roadmap, and differentiators.
3. **Brand & Tone Guidelines**: Ensure narrative voice and formatting comply with corporate standards.
4. **Optional Attachments**: Case studies, pricing tables, implementation playbooks that can be referenced or linked.

## Output Structure
1. **Executive Overview**: Brief recap of customer situation, goals, and how the product addresses them.
2. **Proposed Solution**: Tailored description mapping whitepaper capabilities to customer needs, including deployment approach and timeline highlights.
3. **Value & ROI Justification**: Quantified benefits or qualitative impact statements tied to the customer's stated challenges.
4. **Pricing Placeholder**: Clearly labeled area where account teams can manually insert the latest pricing package before delivery.
5. **Implementation Plan**: High-level phases, responsibilities, and success criteria using available brief data.
6. **Next Steps & Call to Action**: Clear guidance on meetings, approvals, or documentation required to move forward.
7. **Appendix**: Optional section with relevant product specs, security details, or case study references.

## Execution Notes
- Parse the customer brief to extract key entities (stakeholders, initiatives, blockers) and map them to whitepaper sections.
- Allow configuration of proposal depth (concise summary vs. detailed document) and export format (Markdown, PDF-ready HTML, etc.).
- Maintain a library of reusable proposal snippets tied to specific industries or use cases to accelerate personalization.
- Track citations back to the whitepaper and brief so reviewers can verify source sentences.
- Default proposal filenames should follow the convention `<YYYYMMDD>-<CustomerName>-Proposal-R<Revision>` to align with existing version-control practices.

## Open Questions
- Do we need integration hooks for CRM or e-signature platforms to send the proposal once generated?
