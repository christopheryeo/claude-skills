# new-proposal Idea

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
4. **Template Library**: Professionally designed proposal templates (standard business proposal, project bid, service agreement, partnership proposal, grant application) that provide consistent structure across deliverables.
5. **Optional Attachments**: Case studies, pricing tables, implementation playbooks that can be referenced or linked.
6. **Account & Project Metadata**: Client name, industry, contact details, project scope, pricing guidelines, compliance considerations, and target timeline sourced from CRM and discovery artifacts.

## Output Structure
1. **Executive Overview**: Brief recap of customer situation, goals, and how the product addresses them.
2. **Proposed Solution**: Tailored description mapping whitepaper capabilities to customer needs, including deployment approach and timeline highlights.
3. **Value & ROI Justification**: Quantified benefits or qualitative impact statements tied to the customer's stated challenges.
4. **Pricing Placeholder**: Clearly labeled area where account teams can manually insert the latest pricing package before delivery.
5. **Implementation Plan**: High-level phases, responsibilities, and success criteria using available brief data.
6. **Next Steps & Call to Action**: Clear guidance on meetings, approvals, or documentation required to move forward.
7. **Appendix**: Optional section with relevant product specs, security details, or case study references.

### Formatting & Packaging Expectations
- Generate a polished proposal packet that includes a cover page, table of contents, and standard company credentials before the core sections listed above.
- Provide export-ready versions in Markdown for rapid edits and in PDF or DOCX for final delivery, preserving brand styling throughout.
- Maintain clearly labeled placeholders for sensitive items (e.g., pricing tables, legal terms) so account teams can insert the latest approved language prior to sending.

## Execution Notes
- Parse the customer brief to extract key entities (stakeholders, initiatives, blockers) and map them to whitepaper sections.
- Allow configuration of proposal depth (concise summary vs. detailed document) and export format (Markdown, PDF-ready HTML, PDF, DOCX, or shareable link) while keeping `<YYYYMMDD>-<CustomerName>-Proposal-R<Revision>` naming.
- Maintain a library of reusable proposal snippets tied to specific industries or use cases to accelerate personalization.
- Track citations back to the whitepaper and brief so reviewers can verify source sentences.
- Support template-based generation so users can initialize drafts from a chosen blueprint, then inject dynamic content from briefs and whitepapers.
- Offer guided editing commands (e.g., "Update the executive summary to highlight AI integration expertise" or "Include a case study about our recent healthcare project") that modify the draft without breaking structural integrity.
- Capture revision history metadata so teams can compare versions and roll back changes when needed.
- Default proposal filenames should follow the convention `<YYYYMMDD>-<CustomerName>-Proposal-R<Revision>` to align with existing version-control practices.
- Provide export actions ("Export this proposal as a PDF for client review") that bundle the final document and any cited appendices.

## Open Questions
- Do we need integration hooks for CRM or e-signature platforms to send the proposal once generated?
- Should we enforce a minimum set of required fields (e.g., client contact, project scope, compliance constraints) before allowing a proposal export to ensure completeness?
