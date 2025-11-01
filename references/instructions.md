# Step-by-Step Instructions for AI-Generated Skill Creation Document

## Important Context Files

Before beginning skill creation, the AI should have access to and consult the following resources:

1. **claude-skills folder**: Contains existing Claude skills that can be referenced, extended, or leveraged when developing the new skill
2. **claude-connections folder**: Contains available integrations and connections that can enhance the skill's capabilities
3. **how-to-build-claude-skills.md**: Contains best practices and design principles for creating effective Claude skills

The AI should review these resources as needed throughout the skill creation process to ensure alignment with existing skills, leverage available integrations, and follow established best practices.

---

## Step 1: Gather Input
The AI should request and collect:
- **Skill Name**: The identifier for the skill (e.g., `pdf-rotator`, `brand-guidelines`)
- **Skill Description**: A comprehensive description that includes what the skill does and when to use it
- **Optional**: Any specific use cases or examples the user wants to highlight

## Step 2: Analyze the Skill Requirements
Based on the description, the AI should determine:
- **What type of skill** this is (document processing, API integration, workflow automation, reference/knowledge base, etc.)
- **Consult existing skills**: Review the `claude-skills` folder to identify similar or related skills that could be extended, referenced, or leveraged to avoid duplication
- **Evaluate integrations**: Review the `claude-connections` folder to determine if any available integrations can enhance the skill's capabilities
- **What bundled resources** are likely needed:
  - **Scripts**: Repeatable, deterministic code tasks (identify if tasks like file manipulation, data processing, or API calls are involved)
  - **References**: Documentation, schemas, or templates (identify if domain knowledge, configuration, or procedural details are needed)
  - **Assets**: Templates, boilerplate code, or resources for output (identify if templates, icons, or starting files are needed)

## Step 3: Consult Best Practices
The AI should review `how-to-build-claude-skills.md` to ensure the skill design follows established best practices, including:

- **Obvious Name and Purpose**: Ensure the skill has a clear, simple name and a concise description that Claude can easily identify
- **Clear Success Criteria**: Define specific pass/fail conditions for what success looks like
- **Explicit Guard Rails**: Clearly define what the skill should NOT do and what tasks are out of scope
- **Versioning Considerations**: Note that the skill should be designed to work reliably across different versions and contexts
- **Progressive Disclosure**: Keep the SKILL.md body lean (~500 lines) with detailed information in separate reference files
- **Reliability Design**: Treat the skill as a product that will be refined iteratively; avoid cluttering the main context window

## Step 4: Specify the Skill Directory Structure
The AI should output the exact folder structure the user needs to create:
```
skill-name/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Include instructions for creating this structure using standard commands (e.g., `mkdir -p skill-name/{scripts,references,assets}`), but do not actually create the directories themselves.

## Step 5: Generate the SKILL.md File
The AI should create a complete `SKILL.md` with:

**Frontmatter (YAML):**
```yaml
---
name: [skill-name]
description: [comprehensive description provided by user]
license: Complete terms in LICENSE.txt
---
```

**Body (Markdown):**
- A clear title and overview of what the skill does
- Core workflow or main instructions
- **Obvious Name and Purpose**: Reinforce the skill's clear purpose and when it should be triggered
- **Clear Success Criteria**: Document specific pass/fail conditions
- **Explicit Guard Rails**: Clearly state what the skill does NOT do and out-of-scope tasks
- References to bundled resources with clear guidance on when to use them (e.g., "See `scripts/example.py` for automating X" or "Refer to `references/schema.md` for database structure")
- If applicable, reference related skills from the `claude-skills` folder to avoid duplication or to show how this skill extends existing functionality
- Progressive disclosure: keep essential information in SKILL.md (~500 lines max), reference detailed material in separate files
- Use imperative/infinitive form ("Do X," "Create Y," not "The skill creates Y")

## Step 6: Generate Scripts (if applicable)
For each identified script, the AI should:
1. **Determine the script language** based on the task (Python for data processing, Bash for file operations, etc.)
2. **Consult claude-connections** if any scripts need to leverage available integrations
3. **Write complete, working code** that:
   - Includes proper error handling
   - Has clear comments explaining functionality
   - Accepts configurable parameters
   - Returns meaningful output or error messages
4. **Specify the file path** at `scripts/[descriptive-name].[extension]`
5. **Document the script** in SKILL.md with usage examples and parameters
6. **Provide the complete code** ready for the user to copy and paste

Example format for `scripts/example.py`:
```python
#!/usr/bin/env python3
"""
[Clear description of what this script does]

Usage:
    python3 example.py --input <file> --output <file>
"""

import argparse
import sys

def main():
    # Implementation with error handling
    pass

if __name__ == "__main__":
    main()
```

## Step 7: Generate References (if applicable)
For each identified reference document, the AI should:
1. **Create a markdown file** at `references/[topic].md` with:
   - Clear section headers
   - Code examples or templates relevant to the skill
   - Schemas, configurations, or procedural details
   - Links or cross-references to other files as needed
2. **Keep content focused** on domain knowledge that Claude would need while using the skill
3. **Reference it from SKILL.md** with clear trigger conditions (e.g., "See `references/api-docs.md` for endpoint specifications")
4. **Consult how-to-build-claude-skills.md** to ensure reference documents follow best practices for progressive disclosure

## Step 8: Generate Assets (if applicable)
For each identified asset, the AI should:
1. **Determine asset type** (templates, boilerplate code, images, fonts, sample documents)
2. **Consult claude-skills** to see if existing assets can be adapted or reused
3. **Specify the asset path** at `assets/[category]/[filename]`
4. **Reference it from SKILL.md** with clear instructions on how to use it
5. **For templates**: Include placeholders and example usage comments

## Step 9: Create a Comprehensive Implementation Guide (skill-manifest.md)
**Important:** The output generated by following these instructions is itself a step-by-step document called **`skill-manifest.md`**. This manifest is a deliverable that Claude can use with its skill-creator skill to automatically create the actual Claude skill. The manifest contains all file paths, contents, and instructions necessary for Claude to implement the skill without additional input.

The AI should generate a document containing:

### A. Directory Setup Instructions
Provide clear commands to create the directory structure without actually creating it:
```bash
mkdir -p skill-name/{scripts,references,assets}
cd skill-name
```

### B. File Creation Instructions
- Specify that `SKILL.md` should be created with the exact content generated in Step 5
- For each script file: provide the file path and complete code ready to copy-paste
- For each reference file: provide the file path and complete markdown content ready to copy-paste
- For each asset: provide the file path and instructions on how to create or source it

### C. File Contents
- Provide the **exact text** for each file (SKILL.md, all scripts, all references)
- Include file paths and names explicitly
- For scripts: include the full code ready to copy-paste
- Format code blocks clearly with appropriate language tags
- Include best practices from `how-to-build-claude-skills.md` in the instructions where relevant

### D. Integration Recommendations
- If applicable, reference integrations from `claude-connections` that could enhance the skill
- Provide clear guidance on how to configure or use these integrations
- Link to available connections documentation as needed

### E. Related Skills Reference
- If similar skills exist in `claude-skills`, note them and explain how this new skill differs or extends them
- Suggest ways to avoid duplication with existing skills
- Recommend extension points if this skill is meant to build upon existing ones

### F. Next Steps for User
- Instructions to verify all files are in place
- Suggestions for customization or testing (if applicable)
- Reference to the skill-creator guide for running `package_skill.py` when ready to package the skill
- Guidance on progressive refinement: testing the skill with different phrasings and iteratively improving the SKILL.md instructions rather than tweaking prompts

## Step 10: Format the Output Document (skill-manifest.md)
The AI should structure the **skill-manifest.md** document as a clear, step-by-step guide with:
- Section headers for each file to create
- Code blocks with language tags for scripts and markdown
- Clear file path specifications
- Copy-paste ready content
- No ambiguity—every file path and filename explicitly stated
- A preamble noting which context files were consulted and how they informed the design

---

## Example Output Structure

The AI's generated **skill-manifest.md** document might look like:

```markdown
# Skill Creation Manifest: [skill-name]

## Context and Design Process
This manifest was created with consultation of the following resources:
- **claude-skills**: Reviewed for similar/related skills and to avoid duplication
- **claude-connections**: Reviewed for available integrations to enhance capabilities
- **how-to-build-claude-skills.md**: Applied best practices for skill design and reliability

[Document which skills were reviewed, which integrations could be leveraged, and which best practices were applied]

## Overview
[Description provided by user]

## Success Criteria and Guard Rails
- **Success looks like:** [Specific pass/fail conditions]
- **Out of scope:** [What this skill does NOT do]

## Step 1: Create Directory Structure
Run the following command to create the required folders:

\`\`\`bash
mkdir -p skill-name/{scripts,references,assets}
cd skill-name
\`\`\`

## Step 2: Create SKILL.md
**File path:** `skill-name/SKILL.md`

[Complete SKILL.md content goes here]

## Step 3: Create Scripts
### Script 1: [script-name]
**File path:** `skill-name/scripts/[script-name].py`

[Complete working Python code goes here]

### Script 2: [script-name]
**File path:** `skill-name/scripts/[script-name].py`

[Complete working Python code goes here]

## Step 4: Create References
### Reference 1: [reference-name]
**File path:** `skill-name/references/[reference-name].md`

[Complete markdown content goes here]

## Step 5: Create Assets
### Asset 1: [asset-name]
**File path:** `skill-name/assets/[asset-name].ext`

[Asset content or instructions go here]

## Related Skills
- **[existing-skill-name]**: [Brief explanation of relationship and how this skill differs/extends]

## Integration Recommendations
- **[integration-name]**: [Brief explanation of how this integration could enhance the skill]

## Validation & Next Steps
- Verify all files are in place according to the directory structure
- Test the skill with different phrasings to ensure Claude correctly identifies and loads it
- If output is not perfect, refine the SKILL.md instructions rather than changing prompts
- When ready, use the packaging script to create the skill
- Follow progressive refinement practices: start with the core workflow and iteratively improve
```

---

## Summary

By following these instructions, an AI generates a **skill-manifest.md** document that is itself a complete, step-by-step implementation guide. This manifest:

- Consults existing skills, available integrations, and best practices during creation
- Incorporates recommendations for related skills and integration opportunities
- Documents success criteria and guard rails
- Provides all file paths, contents, and instructions necessary for Claude to implement the skill
- Can then be provided to Claude, which can use its skill-creator skill to automatically create the actual Claude skill

The manifest bridges the gap between the initial skill concept (name + description) and the fully implemented, packaged skill ready for distribution, while ensuring alignment with existing skills, best practices, and available capabilities.