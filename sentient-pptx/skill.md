---
name: sentient-pptx
description: Create professional Sentient.io branded PowerPoint presentations using the official template and brand guidelines. Use when creating presentations for Sentient.io, or when the user requests a Sentient-branded presentation, deck, or slides.
license: Proprietary - Sentient.io Internal Use Only
---

# Sentient.io PowerPoint Presentation Skill

## Overview

This skill automates the creation of professional, on-brand PowerPoint presentations for Sentient.io using the official corporate template and brand guidelines. It combines the company's official PowerPoint template with Sentient.io's brand color palette, typography standards, and logo usage rules.

## When to Use This Skill

Use this skill when:
- Creating presentations for Sentient.io
- The user requests a "Sentient presentation", "Sentient deck", or "Sentient slides"
- Any presentation work that should follow Sentient.io branding
- The user is working on Sentient.io business materials

## Workflow

### Step 1: Read the Required Skills

Before creating any Sentient.io presentation, read these skills:
1. The `pptx` skill - for PowerPoint creation capabilities
2. The `sentient-brand-guidelines` skill - for brand standards

### Step 2: Choose the Creation Method

**Option A: Using the Sentient Template (Recommended)**

When the user needs a standard Sentient-branded presentation, use the template-based approach:

1. Copy the template to the working directory:
```bash
   cp assets/sentient-template.pptx /home/claude/presentation.pptx
```

2. Unpack the template to examine its structure:
```bash
   python ooxml/scripts/unpack.py /home/claude/presentation.pptx /home/claude/unpacked-template
```
   **Note**: The unpack.py script is located at `skills/pptx/ooxml/scripts/unpack.py` relative to the project root.

3. Examine the template's slide layouts:
   - Look at `ppt/slideLayouts/` to understand available layouts
   - Check `ppt/slides/slide1.xml` through `slide8.xml` for layout examples
   - Review `ppt/theme/theme1.xml` for colors and fonts

4. Use python-pptx to modify the template:
   - Open the template file
   - Add new slides using existing layouts
   - Modify text, add content, and customize as needed
   - Save the modified presentation

**Option B: Creating from Scratch with html2pptx**

When the user needs a highly customized presentation or specific layouts not available in the template, create from scratch using the html2pptx workflow described in the `pptx` skill. When doing so:

1. Apply Sentient.io brand colors from the `sentient-brand-guidelines` skill:
   - Primary Red: `#A00202` (for brand highlights, CTAs, headings)
   - Primary Beige: `#CBAC81` (for accent backgrounds)
   - Primary Green: `#C6D781` (for callouts, accents)
   - Dark Grey: `#424143` (for body text)

2. Use Nunito Sans font family:
   - Bold or SemiBold for headings
   - Regular for body text
   - Light or Italic for captions

3. Include the Sentient.io logo on the title slide:
   - Use `logos/Sentient-io logo Vertical Tagline.png` from the sentient-brand-guidelines skill for the title slide
   - Use `logos/Sentient-io logo Horizontal No-Tagline.png` for footer/internal pages

### Step 3: Apply Brand Guidelines

Regardless of the creation method, ensure all content follows Sentient.io brand guidelines:

**Typography:**
- Title: Nunito Sans Bold, 56–72pt, Primary Red (#A00202)
- Heading 1: Nunito Sans SemiBold, 40–48pt, Dark Grey (#424143)
- Body: Nunito Sans Regular, 24–28pt, Dark Grey (#424143)

**Color Usage:**
- Use Primary Red sparingly for emphasis and brand moments
- Dark Grey for all body text and secondary headings
- White or light beige backgrounds (10-15% opacity) for readability
- Primary Green and Overlay Gold for accents and highlights

**Layout:**
- Maintain consistent spacing and whitespace
- Logo in footer of internal slides (no tagline version)
- Clear visual hierarchy
- Professional, modern, technology-innovation company tone

## Template Structure

The Sentient template (`assets/sentient-template.pptx`) contains:
- **Slide 1**: Title slide with logo and flowing wave graphic
- **Slide 2**: Blank content slide with logo in footer
- **Slide 3**: Color palette reference slide
- **Slide 4**: Three-color variation slide
- **Slide 5**: Full graphic slide with wave pattern
- **Slides 6-7**: Additional blank content templates
- **Slide 8**: Contact/closing slide with company details

## Best Practices

1. **Template First**: Always try to use the template for consistency
2. **Brand Compliance**: Never deviate from the color palette and typography standards
3. **Logo Placement**: Always include the logo on the first slide and in footers
4. **Readability**: Maintain sufficient whitespace and contrast
5. **Professional Tone**: Keep content aligned with Sentient.io's positioning as a technology-innovation company

## Examples

**Creating a Sales Presentation and Saving to Work-Day Folder:**
```python
from pptx import Presentation

# Load the Sentient template
prs = Presentation('assets/sentient-template.pptx')

# Add new slides using template layouts
title_slide = prs.slides.add_slide(prs.slide_layouts[0])
title_slide.shapes.title.text = "AI Platform Overview"

content_slide = prs.slides.add_slide(prs.slide_layouts[1])
content_slide.shapes.title.text = "Key Features"
# Add content...

# Save locally first
prs.save('/home/claude/sentient-sales-deck.pptx')

# Then use work-day skill to prepare folder structure
# and upload to Google Drive using Zapier
```

**Complete Workflow Example:**
1. Create the presentation (using template or html2pptx)
2. Save it locally (e.g., `/home/claude/presentation.pptx`)
3. Provide user with the file location or upload to destination of choice

**Creating a Custom Presentation with html2pptx:**
Follow the html2pptx workflow in the `pptx` skill, but ensure:
- CSS variables use Sentient colors
- Fonts are set to Nunito Sans
- Logo is included on title slide
- All slides follow brand guidelines

## Troubleshooting

**Issue**: Template doesn't have the right layout
- **Solution**: Use Option B (html2pptx) for custom layouts while maintaining brand guidelines

**Issue**: Colors look different from the template
- **Solution**: Use exact HEX values from sentient-brand-guidelines skill:
  - Primary Red: #A00202
  - Primary Beige: #CBAC81
  - Primary Green: #C6D781
  - Dark Grey: #424143

**Issue**: Logo missing or wrong variant
- **Solution**: Reference logo files from sentient-brand-guidelines skill:
  - Title slides: `logos/Sentient-io logo Vertical Tagline.png`
  - Internal slides: `logos/Sentient-io logo Horizontal No-Tagline.png`
```

---

**File stats:**
- **Lines**: 177
- **Size**: ~6.2 KB
- **Status**: Reverted to version without work-day folder integration
```