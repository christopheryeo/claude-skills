# Google Drive Topic Query Cheatsheet

Use these patterns when constructing topic-focused Drive searches.

## Core Operators

| Need | Operator | Example |
|------|----------|---------|
| Exact phrase | `"phrase"` | `"brand manifesto"` |
| Any of multiple terms | `(term1 OR term2)` | `(apollo OR "project apollo")` |
| Exclude term | `-term` | `-draft` |
| File type | `type:` or `mimeType=` | `type:presentation` or `mimeType=application/pdf` |
| Owner filter | `owner:` | `owner:designlead@company.com` |
| Shared drive | `parent:` with drive ID | `parent:0ADriveSharedID` |
| Updated after date | `modifiedTime >` | `modifiedTime > 2025-07-01T00:00:00` |

Combine operators to mirror the user's topic description, ensuring parentheses wrap OR conditions before adding exclusions.

## Sample Queries

- **Launch campaign decks**: `"Launch Plan" AND type:presentation AND ("Nova" OR "NVA")`
- **Client research docs**: `("client brief" OR "discovery memo") AND owner:account.team@company.com`
- **Exclude archived work**: `"pricing model" -"archive" -parent:0AOldDriveID`

## Result Quality Tips

1. Start narrow with exact phrases, then broaden by removing quotes or exclusions if results < 5.
2. Use `in:` filters (e.g., `in:trash`, `in:teamDrive`) only when necessary; default search already covers active files.
3. Respect permission flags: if a file returns `Access denied`, surface the metadata but note the restriction.
