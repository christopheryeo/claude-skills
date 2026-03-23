#!/usr/bin/env python3
"""
News Articles Rename Script
Extracts article headlines from PDF and image files using OCR,
then renames the files to their article titles.

Handles common newspaper layout patterns:
- Headlines that wrap across multiple short lines
- Section labels like "News analysis", "Announcement" appearing before the real headline
- Single blank lines within a headline block
- OCR artifacts and metadata lines
"""

import os
import sys
import re
import json
import time
import shutil
from pathlib import Path

import pytesseract
from PIL import Image
from pdf2image import convert_from_path


# Section headers and metadata patterns to skip when looking for headlines
SKIP_PATTERNS = [
    r"^the\s+straits\s+times",
    r"^straits\s+times",
    r"^(monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
    r"^(january|february|march|april|may|june|july|august|september|october|november|december)",
    r"^\d{1,2}\s+(january|february|march|april|may|june|july|august|september|october|november|december)",
    r"^(singapore|world|business|forum|sport|sports|life|lifestyle|opinion|asia|asean|tech|money|invest|property|food|home|health|science|environment|politics|big\s+read|top\s+of\s+the\s+news|multimedia|photo)$",
    r"^news\s+analysis$",
    r"^(commentary|editorial|feature|special\s+report|exclusive|review|interview|profile|obituary)$",
    r"^page\s*\d+",
    r"^\d+$",
    r"^[a-z]\d+$",  # e.g. "A12", "B3"
    r"^https?://",
    r"^www\.",
    r"^©",
    r"^(continued|cont['']?d)\s+(from|on)",
    r"^(source|photo|image|graphic|illustration|chart)\s*:",
    r"^(advertisement|sponsored|advert)",
    r"^st\s+photo",
    r"^(file\s+)?photo",
]

SKIP_RE = [re.compile(p, re.IGNORECASE) for p in SKIP_PATTERNS]

# Characters not allowed in filenames
UNSAFE_CHARS = re.compile(r'[/\\:*?"<>|]')

SUPPORTED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}


def is_skip_line(line: str) -> bool:
    """Check if a line looks like metadata rather than a headline."""
    stripped = line.strip()
    if len(stripped) < 4:
        return True
    for pattern in SKIP_RE:
        if pattern.search(stripped):
            return True
    return False


def is_body_text(line: str) -> bool:
    """
    Detect if a line looks like the start of article body text rather than headline.
    Body text tends to be longer, contains punctuation patterns typical of prose,
    and often starts with a dateline or byline.
    """
    stripped = line.strip()
    # Byline patterns: "Kok Yufeng", "Senior Business Correspondent", etc.
    if re.match(r"^(by\s+)", stripped, re.IGNORECASE):
        return True
    if re.match(r"^[A-Z][a-z]+\s+[A-Z][a-z]+$", stripped):
        # Two capitalized words alone on a line = likely a byline name
        return True
    if re.match(r"^(Senior\s+|Chief\s+|Deputy\s+|Assistant\s+)?(Business\s+|Political\s+|Foreign\s+|Regional\s+)?(Correspondent|Reporter|Editor|Writer|Columnist|Bureau\s+Chief)", stripped, re.IGNORECASE):
        return True
    if re.match(r"^Correspondent$", stripped, re.IGNORECASE):
        return True
    # Dateline: "SINGAPORE - ", "NEW DELHI ~ ", "MEXICO CITY -"
    if re.match(r"^[A-Z]{3,}(\s+[A-Z]{3,})*\s*[-~—–]", stripped):
        return True
    # Very long lines are usually body text, not headlines
    if len(stripped) > 150:
        return True
    return False


def extract_text_from_pdf(filepath: str) -> str:
    """Convert first page of PDF to image and run OCR."""
    try:
        images = convert_from_path(filepath, first_page=1, last_page=1, dpi=300)
        if not images:
            return ""
        return pytesseract.image_to_string(images[0], lang="eng")
    except Exception as e:
        print(f"  Warning: PDF conversion failed for {filepath}: {e}", file=sys.stderr)
        return ""


def extract_text_from_image(filepath: str) -> str:
    """Run OCR directly on an image file."""
    try:
        img = Image.open(filepath)
        return pytesseract.image_to_string(img, lang="eng")
    except Exception as e:
        print(f"  Warning: Image OCR failed for {filepath}: {e}", file=sys.stderr)
        return ""


def extract_headline(text: str) -> str | None:
    """
    Extract the most likely headline from OCR text.

    Newspaper headlines are visually prominent and appear near the top of the page.
    They often wrap across multiple short lines in OCR output because the large font
    means fewer words fit per line. The strategy:

    1. Skip metadata lines (newspaper name, date, section labels)
    2. Collect the first block of substantial lines as the headline
    3. A blank line ends the headline UNLESS the headline so far is very short
       (< 30 chars), in which case it continues past one blank line
    4. Stop when we hit body text, a byline, or a second text block
    """
    if not text or not text.strip():
        return None

    lines = text.split("\n")
    headline_parts = []
    found_start = False
    hit_blank_after_start = False

    for line in lines:
        stripped = line.strip()

        # Handle blank / whitespace-only lines
        if not stripped or len(stripped.strip()) <= 1:
            if found_start:
                current_headline = " ".join(headline_parts)
                # If headline is already substantial, a blank line means it's done
                if len(current_headline) >= 30:
                    break
                # Short headline — might continue past blank (e.g. wrapped title)
                hit_blank_after_start = True
            continue

        # Skip metadata lines (newspaper name, date, section labels)
        if is_skip_line(stripped):
            if found_start:
                # Already collecting headline — metadata means it's done
                break
            continue

        # Stop if we hit body text (datelines, bylines, long prose lines)
        if is_body_text(stripped):
            break

        # If we already collected a block and crossed a blank line,
        # this is the second text block (sub-headline) — stop,
        # UNLESS the headline so far is still very short (< 30 chars),
        # which means the blank was within a wrapped headline
        if found_start and hit_blank_after_start:
            current_headline = " ".join(headline_parts)
            if len(current_headline) >= 30:
                break
            # Short headline — continue collecting past the blank
            hit_blank_after_start = False

        # This looks like headline text
        found_start = True
        headline_parts.append(stripped)

        # Safety: headlines rarely exceed 8 wrapped lines
        if len(headline_parts) >= 8:
            break

    if not headline_parts:
        return None

    headline = " ".join(headline_parts)

    # Clean up common OCR artifacts
    headline = headline.strip()
    headline = re.sub(r"\s+", " ", headline)
    # Fix common OCR misreads
    headline = re.sub(r"\bAl\b", "AI", headline)  # "Al" → "AI" (common OCR error)
    headline = headline.rstrip(".")  # Remove trailing period (not typical in headlines)

    # If headline is unreasonably short, it's probably wrong
    if len(headline) < 10:
        return None

    return headline


def sanitise_filename(title: str, extension: str) -> str:
    """Make a title safe for use as a filename."""
    # Remove unsafe characters
    safe = UNSAFE_CHARS.sub("", title)
    # Collapse multiple spaces
    safe = re.sub(r"\s+", " ", safe).strip()
    # Trim length
    max_len = 120 - len(extension)
    if len(safe) > max_len:
        safe = safe[:max_len].rstrip()
    return f"{safe}{extension}" if safe else None


def unique_path(directory: Path, filename: str) -> Path:
    """Generate a unique filepath, appending (2), (3), etc. if needed."""
    target = directory / filename
    if not target.exists():
        return target
    stem = Path(filename).stem
    ext = Path(filename).suffix
    counter = 2
    while True:
        candidate = directory / f"{stem} ({counter}){ext}"
        if not candidate.exists():
            return candidate
        counter += 1


def copy_with_retry(src: str, dst: str, max_retries: int = 5, delay: float = 1.0) -> bool:
    """Copy a file with retries to handle filesystem lock issues on mounted drives."""
    for attempt in range(max_retries):
        try:
            shutil.copy2(src, dst)
            return True
        except OSError:
            if attempt < max_retries - 1:
                time.sleep(delay)
    return False


def process_folder(folder_path: str) -> list[dict]:
    """Process all supported files in the folder and rename them."""
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Collect files to process
    files = sorted([
        f for f in folder.iterdir()
        if f.is_file()
        and not f.name.startswith(".")
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ])

    if not files:
        print("No supported files found in the folder.")
        return []

    results = []
    print(f"Found {len(files)} file(s) to process.\n")

    # Use a temp directory for processing if files might be on a mounted drive
    # This avoids filesystem lock issues during OCR
    import tempfile
    temp_dir = tempfile.mkdtemp(prefix="news_rename_")
    use_temp = False

    # Test if we can read files directly
    try:
        with open(str(files[0]), "rb") as f:
            f.read(16)
    except OSError:
        use_temp = True
        print("Mounted filesystem detected — copying files locally for processing.\n")

    for i, filepath in enumerate(files, 1):
        original_name = filepath.name
        ext = filepath.suffix.lower()
        print(f"[{i}/{len(files)}] Processing: {original_name}")

        # If on mounted drive, copy to temp first
        work_path = str(filepath)
        if use_temp:
            temp_file = os.path.join(temp_dir, original_name)
            if not copy_with_retry(str(filepath), temp_file):
                results.append({
                    "original": original_name,
                    "new": original_name,
                    "status": "error",
                    "headline": None,
                    "error": "Could not read file (filesystem lock)",
                })
                print(f"  ✗ Could not read file after retries")
                continue
            work_path = temp_file

        # Extract text via OCR
        if ext == ".pdf":
            text = extract_text_from_pdf(work_path)
        else:
            text = extract_text_from_image(work_path)

        # Find headline
        headline = extract_headline(text)

        if headline:
            new_filename = sanitise_filename(headline, ext)
            if new_filename and new_filename != original_name:
                new_path = unique_path(folder, new_filename)
                try:
                    filepath.rename(new_path)
                    results.append({
                        "original": original_name,
                        "new": new_path.name,
                        "status": "renamed",
                        "headline": headline,
                    })
                    print(f"  → Renamed to: {new_path.name}")
                except OSError as e:
                    results.append({
                        "original": original_name,
                        "new": original_name,
                        "status": "error",
                        "headline": headline,
                        "error": str(e),
                    })
                    print(f"  ✗ Rename failed: {e}")
            else:
                results.append({
                    "original": original_name,
                    "new": original_name,
                    "status": "skipped",
                    "headline": headline,
                    "reason": "sanitised name same as original or empty",
                })
                print(f"  – Skipped (name unchanged)")
        else:
            results.append({
                "original": original_name,
                "new": original_name,
                "status": "no_title",
                "headline": None,
            })
            print(f"  ⚠ No headline found, keeping original name")

    # Clean up temp directory
    if use_temp:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return results


def print_summary(results: list[dict]):
    """Print a summary table of results."""
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    renamed = sum(1 for r in results if r["status"] == "renamed")
    failed = sum(1 for r in results if r["status"] in ("no_title", "error"))
    skipped = sum(1 for r in results if r["status"] == "skipped")

    for i, r in enumerate(results, 1):
        status_icon = {
            "renamed": "✅",
            "no_title": "⚠️",
            "error": "❌",
            "skipped": "⏭️",
        }.get(r["status"], "?")
        print(f"  {i}. {status_icon} {r['original']}")
        if r["status"] == "renamed":
            print(f"     → {r['new']}")
        elif r["status"] == "error":
            print(f"     Error: {r.get('error', 'unknown')}")
        elif r["status"] == "no_title":
            print(f"     (no headline detected)")

    print(f"\nTotal: {len(results)} | Renamed: {renamed} | No title: {failed} | Skipped: {skipped}")

    # Also save results as JSON for programmatic access
    results_path = Path(sys.argv[1]) / ".rename_results.json"
    try:
        with open(results_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nDetailed results saved to: {results_path}")
    except Exception:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <folder-path>", file=sys.stderr)
        sys.exit(1)

    results = process_folder(sys.argv[1])
    if results:
        print_summary(results)
