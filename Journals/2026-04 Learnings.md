# 2026-04 Learnings

## 2026-04-01

- **Skills library workspace-to-live sync gap.** 5 skills have development folders in the workspace root but are not deployed to `.claude/skills/` (list-files, new-proposal, new-quotation, project-pulse-brief, smartchat-service-costs), while 8 live skills have no workspace development folder (algorithmic-art, brand-guidelines, docx, pdf, pptx, schedule, skill-creator, xlsx). The workspace is not a reliable single source of truth for the library's deployment state — a reconciliation pass or deployment manifest is needed.

- **daily-plans storage delegation has an inconsistent write path.** daily-plans delegates all content creation to daily-journals sub-commands (CREATE → CREATE-JOURNAL + CREATE-ENTRY; NEW → CREATE-ENTRY; LOG → NEW → CREATE-ENTRY). However, EXECUTE and DELETE bypass daily-journals entirely and perform direct file edits on the Plans journal. This means changes to daily-journals' insertion or formatting logic would not propagate to EXECUTE/DELETE operations, creating a potential consistency risk.

- **Knowledge Fabric index file is missing.** The daily-knowledge skill's CLASSIFY and FILE sub-commands depend on `Knowledge/knowledge_fabric.md` as the single source of truth for routing knowledge across the three knowledge layers. This file does not exist in the current workspace — the Knowledge folder contains only reference documents (Skills_Comparison, daily-calendars-eval, schedule, etc.). CLASSIFY and FILE cannot function as designed until the fabric is created or restored.
