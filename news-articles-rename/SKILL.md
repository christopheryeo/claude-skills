---
name: news-articles-rename
description: >
  OCR and rename news article files (PDFs and images) by extracting the article headline from
  the content and using it as the filename. Targets the Vivien (PA)/News/ folder. Use this skill
  whenever the user asks to rename news articles, organise news clippings, process newspaper
  PDFs, extract article titles from scanned pages, or tidy up the News folder. Also trigger when
  the user mentions "rename articles", "news folder", "article titles", or "news clippings".
---

# News Articles Rename

## Purpose

Newspaper articles saved as PDFs or images typically arrive with unhelpful filenames like
`Image 2026-02-25 15-52-38.pdf`. This skill extracts the main headline from each file using
OCR and renames it to `Article Title.pdf` — making the News folder instantly browsable.

## Target Folder

The default target is always:

```
Vivien (PA)/News/
```

## Supported File Types

Process any file with these extensions: `.pdf`, `.png`, `.jpg`, `.jpeg`

Skip hidden files (starting with `.`) and any file that doesn't match these extensions.

## How It Works

Run the bundled script `scripts/rename_articles.py` which handles the full pipeline:

```bash
python3 <skill-path>/scripts/rename_articles.py "<news-folder-path>"
```

The script will:
1. Scan the folder for all supported files
2. For each file, extract the first page as an image (300 DPI)
3. Run Tesseract OCR on the image
4. Identify the headline using heuristics (skip metadata, collect first substantial text block)
5. Apply common OCR corrections (e.g. "Al" → "AI")
6. Sanitise the headline for use as a filename
7. Rename the file, handling duplicates by appending a number
8. Print a summary table of old → new filenames

The script also handles mounted filesystem lock issues automatically by copying files to a
temp directory for OCR processing when direct reads fail.

## After Running

Present the results as a clear summary table showing what was renamed:

| # | Original Filename | New Filename | Status |
|---|---|---|---|
| 1 | Image 2026-02-25 15-52-38.pdf | Headline Goes Here.pdf | ✅ Renamed |
| 2 | Image 2026-02-25 15-53-03.pdf | Another Article.pdf | ✅ Renamed |
| 3 | some-file.png | some-file.png | ⚠️ No title found |

Flag any files that couldn't be processed and explain why. Note that minor OCR artefacts
in headlines (e.g. misread characters) are expected from Tesseract — only flag files where
no headline could be extracted at all.

## Important Notes

- Always process **every** file in the folder. Do not leave any file out.
- If OCR is uncertain about a headline, prefer keeping the original name over guessing wrong.
- The script handles both single-page and multi-page PDFs — only the first page is used for title extraction.
- For image files (.png, .jpg, .jpeg), OCR is run directly on the image.
