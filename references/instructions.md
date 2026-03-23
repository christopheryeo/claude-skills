## Step-by-Step Instructions for AI-Generated Skill Creation Document (OpenAI Codex Edition)

### Important Context Files

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
- **Target Audience**: Who will use this skill (e.g., developers, designers, content creators)
- **Primary Use Case**: The main workflow this skill enables
- **Optional**: Any specific use cases or examples the user wants to highlight

**Codex Optimization**: Frame requests as natural language prompts to Codex for clarity.

---

## Step 2: Analyze the Skill Requirements
Based on the description, the AI should determine:

### 2.1 Skill Type Classification
Identify which category the skill falls into:
- **Document Processing** (e.g., PDF manipulation, text extraction, format conversion)
- **API Integration** (e.g., third-party service integration, data synchronization)
- **Workflow Automation** (e.g., multi-step task orchestration, conditional logic)
- **Reference/Knowledge Base** (e.g., domain-specific documentation, configuration guides)
- **Data Transformation** (e.g., format conversion, validation, enrichment)
- **Code Generation** (e.g., boilerplate creation, scaffolding)

### 2.2 Consult Existing Skills
Review the `claude-skills` folder to:
- Identify similar or related skills that could be extended or referenced
- Avoid duplication of functionality
- Determine if this skill should complement or extend existing skills
- Note skills that share similar workflows or patterns

**Output Format**: Document 2-3 related skills with brief explanations of relationship.

### 2.3 Evaluate Integrations
Review the `claude-connections` folder to determine:
- Which available integrations could enhance the skill's capabilities
- Whether any integrations provide pre-built solutions to common problems
- Integration prerequisites (API keys, authentication, rate limits)
- Whether the skill should be standalone or integrate with external systems

**Output Format**: List integrations with proposed use cases (see Step 6.1).

### 2.4 Determine Bundled Resources
Identify what resources the skill will need:

**Scripts** (code-based, repeatable tasks):
- File manipulation (reading, writing, transforming files)
- Data processing (parsing, validating, transforming data structures)
- API calls (making authenticated requests, handling responses)
- System operations (executing shell commands, managing processes)
- Automation logic (conditional workflows, error handling)

**References** (documentation, knowledge, configuration):
- Domain knowledge (industry standards, best practices)
- API documentation (endpoint specs, authentication, response formats)
- Configuration templates (environment variables, config files)
- Procedural guides (step-by-step workflows)
- Schema definitions (data structures, validation rules)

**Assets** (templates, boilerplate, resources):
- Code templates (starter files, boilerplate code)
- Document templates (form templates, document structures)
- Configuration examples (sample config files)
- Sample data (test data, mock responses)

---

## Step 3: Consult Best Practices
The AI should review `how-to-build-claude-skills.md` and apply:

### 3.1 Obvious Name and Purpose
- Skill name must be immediately recognizable and self-explanatory
- Avoid ambiguous or generic names (e.g., use `pdf-merger` instead of `file-handler`)
- Include the skill's primary purpose in the description (first sentence)

### 3.2 Clear Success Criteria
Define specific, testable conditions for skill success:
- **Input validation**: What constitutes valid input?
- **Output validation**: What should successful output look like?
- **Pass/Fail conditions**: Under what conditions does the skill fail?
- **Edge cases**: How should the skill handle boundary conditions?

Example format:
```
SUCCESS: Script correctly merges 2-5 PDFs, producing a single valid PDF file
FAILURE: Input contains non-PDF files, or output file cannot be created
EDGE CASE: Handling PDFs with different page sizes or security settings
```

### 3.3 Explicit Guard Rails
Clearly define scope boundaries:
- **What the skill DOES**: Specific, narrow functionality
- **What the skill DOES NOT**: Explicitly list out-of-scope tasks
- **Limitations**: Known constraints or prerequisites
- **Assumptions**: Dependencies on external systems or user setup

Example format:
```
DOES: Merge PDFs from a local directory
DOES NOT: Download PDFs from URLs, compress PDFs, or extract text
LIMITATIONS: Requires poppler-utils to be installed; max 50 files
ASSUMES: User has write permissions to output directory
```

### 3.4 Versioning Considerations
- Design for robustness across Codex versions
- Avoid version-specific features or deprecated APIs
- Include version detection logic where applicable
- Document required library/tool versions

### 3.5 Progressive Disclosure
- Keep `SKILL.md` body lean (~500 lines maximum)
- Move detailed information to separate reference files
- Reference files with clear trigger conditions (e.g., "See `references/api-schema.md` if integrating with Stripe")
- Use consistent cross-reference formatting

### 3.6 Reliability Design
- Treat the skill as a product subject to iterative refinement
- Include error messages that help users debug issues
- Avoid cluttering the main context window with verbose explanations
- Test scripts thoroughly before delivery (see Step 8)

---

## Step 4: Specify the Skill Directory Structure
The AI should output the exact folder structure the user needs to create:

```
skill-name/
├── SKILL.md                          # Main skill definition
├── LICENSE.txt                       # License terms
├── scripts/                          # Executable code
│   ├── main.py                      # Primary script
│   ├── helpers.py                   # Utility functions
│   └── validate.py                  # Validation script
├── references/                       # Documentation & guides
│   ├── api-schema.md                # API specifications
│   ├── configuration.md             # Config guide
│   └── troubleshooting.md           # Common issues
└── assets/                          # Templates & samples
    ├── templates/                   # Document/code templates
    ├── samples/                     # Example data
    └── config/                      # Configuration examples
```

**Directory Creation Instructions** (for user to execute):
```bash
mkdir -p skill-name/{scripts,references,assets/{templates,samples,config}}
cd skill-name
touch SKILL.md LICENSE.txt
```

Do not create directories; provide commands for the user to execute.

---

## Step 5: Generate the SKILL.md File

### 5.1 Frontmatter (YAML)
```yaml
---
name: [skill-name]
description: [comprehensive description provided by user]
license: Complete terms in LICENSE.txt
version: 1.0.0
author: [User Name]
created: [YYYY-MM-DD]
keywords: [comma-separated keywords for discovery]
---
```

### 5.2 Body Structure (Markdown)

#### 5.2.1 Title & Overview
```markdown
# [Skill Name]

## Overview
[1-2 paragraph description of what the skill does and when to use it]

## Quick Start
[Minimal example showing basic usage]
```

#### 5.2.2 Core Workflow
```markdown
## How It Works
1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

## Key Features
- [Feature 1]: [Brief description]
- [Feature 2]: [Brief description]
- [Feature 3]: [Brief description]
```

#### 5.2.3 Success Criteria & Guard Rails
```markdown
## Success Criteria
**The skill succeeds when:**
- [Specific condition 1]
- [Specific condition 2]
- [Output meets: specific format/quality criteria]

## What This Skill Does
✓ [Does X]
✓ [Does Y]
✓ [Does Z]

## What This Skill Does NOT Do
✗ [Does not do A]
✗ [Does not do B]
✗ [Out of scope: C]

## Limitations & Prerequisites
- **Requires**: [Tool/library version requirements]
- **Assumes**: [User setup assumptions]
- **Limitations**: [Known constraints]
```

#### 5.2.4 Usage Instructions
```markdown
## Usage

### Basic Usage
[Command-line or programmatic example]

### Advanced Usage
[Complex examples with options/flags]

### Configuration
Refer to `references/configuration.md` for environment setup and advanced options.
```

#### 5.2.5 Scripts Reference
```markdown
## Scripts

### Primary Script: `scripts/main.py`
**Purpose**: [What this script does]
**Usage**: 
\`\`\`bash
python3 scripts/main.py --input <file> --output <file> [options]
\`\`\`
**Parameters**:
- `--input`: [Description]
- `--output`: [Description]
- `--verbose`: Enable debug logging

See `scripts/main.py` for full implementation and error handling.

### Helper Script: `scripts/helpers.py`
**Purpose**: [Utility functions for X]
**Usage**: Import in other scripts via `from helpers import function_name`

### Validation Script: `scripts/validate.py`
**Purpose**: Verify input files and configurations before processing
**Usage**: 
\`\`\`bash
python3 scripts/validate.py --input <file>
\`\`\`
```

#### 5.2.6 Integration Recommendations
```markdown
## Integration Opportunities

### [Integration Name] Integration
**Purpose**: [How this integration enhances the skill]
**Proposed Implementation**: [Brief description of what would be integrated]
**Prerequisites**: [API keys, setup requirements]
**Usage Context**: Use this integration when [specific scenario]

See `references/integration-[name].md` for configuration details.
```

#### 5.2.7 Related Skills & Extensions
```markdown
## Related Skills
- **[existing-skill-name]**: [Brief explanation of relationship]
  - *This skill differs by*: [Key differences]
  - *Can be used together with*: [Complementary workflows]

## Extending This Skill
To extend this skill with new functionality:
1. Add new scripts to `scripts/` following the naming convention
2. Update this SKILL.md with new usage examples
3. Add documentation to `references/` if adding significant features
```

#### 5.2.8 Troubleshooting & Support
```markdown
## Common Issues

**Issue**: [Description of common error]
**Solution**: [How to resolve]

**Issue**: [Another common error]
**Solution**: [How to resolve]

For more detailed troubleshooting, see `references/troubleshooting.md`.
```

#### 5.2.9 Version & Change Log
```markdown
## Version History
- **1.0.0** (2024-XX-XX): Initial release
  - Core functionality: [what's included]
  - Tested with: [Python version, dependencies]
```

**Important**: Keep SKILL.md at approximately 500 lines or less. Move detailed content to references.

---

## Step 6: Generate Scripts (if applicable)

### 6.1 Script Generation Process

For each identified script, follow this process:

#### 6.1.1 Determine Script Language
Choose based on task type:
- **Python 3.8+**: Data processing, file manipulation, API integration, cross-platform tasks
- **Bash**: File system operations, system administration, Unix tool chaining
- **JavaScript/Node.js**: Browser automation, JSON manipulation, npm-ecosystem tasks
- **SQL**: Database operations, data querying (if applicable)

**Recommendation**: Default to Python 3 for Codex skills for maximum portability and readability.

#### 6.1.2 Script Architecture Template
All scripts should follow this structure:

```python
#!/usr/bin/env python3
"""
[One-line summary of script purpose]

[2-3 sentence description of what this script does and when to use it]

Usage:
    python3 script_name.py --input <path> --output <path> [options]
    python3 script_name.py --config <config.json>

Exit Codes:
    0: Success
    1: Invalid input or configuration
    2: File not found or permission denied
    3: Processing error (see logs)
    4: Output write failed

Examples:
    # Basic usage
    python3 script_name.py --input data.txt --output result.txt
    
    # With options
    python3 script_name.py --input data.txt --output result.txt --verbose
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('script.log')
    ]
)
logger = logging.getLogger(__name__)


class ScriptError(Exception):
    """Base exception for script errors"""
    pass


class ValidationError(ScriptError):
    """Raised when input validation fails"""
    pass


class ProcessingError(ScriptError):
    """Raised when processing encounters an error"""
    pass


def validate_input(input_path: str) -> Path:
    """
    Validate that input file exists and is readable.
    
    Args:
        input_path: Path to input file
        
    Returns:
        Path object if valid
        
    Raises:
        ValidationError: If file does not exist or is not readable
    """
    try:
        path = Path(input_path)
        if not path.exists():
            raise ValidationError(f"Input file not found: {input_path}")
        if not path.is_file():
            raise ValidationError(f"Input path is not a file: {input_path}")
        if not path.stat().st_size > 0:
            raise ValidationError(f"Input file is empty: {input_path}")
        logger.info(f"✓ Input validated: {path}")
        return path
    except OSError as e:
        raise ValidationError(f"Cannot read input file: {e}")


def validate_output_path(output_path: str) -> Path:
    """
    Validate that output path is writable.
    
    Args:
        output_path: Path where output will be written
        
    Returns:
        Path object if valid
        
    Raises:
        ValidationError: If output path is not writable
    """
    try:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        # Test write permission
        test_file = path.parent / '.write_test'
        test_file.touch()
        test_file.unlink()
        logger.info(f"✓ Output path validated: {path}")
        return path
    except (OSError, PermissionError) as e:
        raise ValidationError(f"Cannot write to output path: {e}")


def process_data(input_data: Any, options: Dict[str, Any]) -> Any:
    """
    Core processing function [REPLACE WITH ACTUAL LOGIC].
    
    Args:
        input_data: Parsed input data
        options: Configuration options from command line
        
    Returns:
        Processed data
        
    Raises:
        ProcessingError: If processing fails
    """
    try:
        logger.info("Starting data processing...")
        
        # TODO: Implement core processing logic here
        # This is a template; replace with actual implementation
        
        logger.info("✓ Processing completed successfully")
        return input_data
    except Exception as e:
        raise ProcessingError(f"Processing failed: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to input file'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Path to output file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--config', '-c',
        help='Optional configuration file (JSON)'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        # Validate inputs
        input_path = validate_input(args.input)
        output_path = validate_output_path(args.output)
        
        # Load configuration if provided
        options = {}
        if args.config:
            try:
                with open(args.config, 'r') as f:
                    options = json.load(f)
                logger.info(f"✓ Loaded configuration: {args.config}")
            except (json.JSONDecodeError, OSError) as e:
                raise ValidationError(f"Cannot load config: {e}")
        
        # Process data
        with open(input_path, 'r') as f:
            input_data = json.load(f) if input_path.suffix == '.json' else f.read()
        
        output_data = process_data(input_data, options)
        
        # Write output
        with open(output_path, 'w') as f:
            if isinstance(output_data, dict):
                json.dump(output_data, f, indent=2)
            else:
                f.write(str(output_data))
        
        logger.info(f"✓ Output written: {output_path}")
        print(f"SUCCESS: Output written to {output_path}")
        return 0
        
    except ValidationError as e:
        logger.error(f"✗ Validation error: {e}")
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    except ProcessingError as e:
        logger.error(f"✗ Processing error: {e}")
        print(f"ERROR: {e}", file=sys.stderr)
        return 3
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}", exc_info=True)
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        return 4


if __name__ == '__main__':
    sys.exit(main())
```

### 6.2 Script Testing & Validation (CRITICAL)

**Before delivery, the AI must validate each script:**

#### 6.2.1 Static Code Analysis
- [ ] All imports are standard library or commonly available packages
- [ ] No hardcoded paths or credentials
- [ ] All functions have docstrings
- [ ] Type hints are present for function parameters and returns
- [ ] Exception handling covers all failure modes
- [ ] Logging is implemented with appropriate levels (DEBUG, INFO, WARNING, ERROR)
- [ ] Exit codes follow Unix conventions (0=success, >0=failure)
- [ ] Error messages are user-friendly and actionable

#### 6.2.2 Functional Validation
For each script, the AI should:

1. **Trace execution paths**: Walk through code with sample inputs to verify logic
2. **Identify edge cases**: Document how script handles:
   - Empty input files
   - Malformed data
   - Missing files
   - Permission errors
   - Very large files
   - Special characters/encoding issues

3. **Verify error handling**: Each exception path should:
   - Log the error with context
   - Return appropriate exit code
   - Provide user-friendly error message
   - Not leave partial output files

4. **Check dependencies**: Document any required packages with versions:
   ```python
   # Required packages:
   # - requests>=2.28.0
   # - pydantic>=1.9.0
   # Install: pip install -r requirements.txt
   ```

#### 6.2.3 Validation Checklist (Output in SKILL.md)
```markdown
## Testing Results

**Script**: `scripts/main.py`
- [x] Handles empty input gracefully (exit code 1)
- [x] Handles missing files (exit code 2)
- [x] Processes valid input correctly (exit code 0)
- [x] Produces valid output format
- [x] Logs all operations appropriately
- [x] Cleans up temporary files on error
- [x] Works with files up to 1GB
- [x] Handles special characters in filenames

**Dependencies**: Python 3.8+, [package list]
**Tested with**: Python 3.10, [dependency versions]
```

#### 6.2.4 Integration Testing
If script uses integrations:
- [ ] Script correctly authenticates with service
- [ ] Script handles API rate limits
- [ ] Script handles API errors gracefully
- [ ] Script includes retry logic with exponential backoff
- [ ] Sensitive data (API keys) are not logged

#### 6.2.5 Documentation of Test Cases
For each script, document test cases in a `tests/` directory:

**File**: `tests/test_main.py`
```python
"""
Test cases for scripts/main.py

Run with: python -m pytest tests/test_main.py -v
"""

import pytest
import tempfile
from pathlib import Path
from scripts.main import validate_input, process_data, ValidationError

class TestValidation:
    """Test input validation"""
    
    def test_valid_input(self):
        """Should accept valid input files"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write('test data')
            f.flush()
            result = validate_input(f.name)
            assert result.exists()
    
    def test_missing_file(self):
        """Should reject missing files"""
        with pytest.raises(ValidationError):
            validate_input('/nonexistent/file.txt')
    
    def test_empty_file(self):
        """Should reject empty files"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.flush()
            with pytest.raises(ValidationError):
                validate_input(f.name)

class TestProcessing:
    """Test data processing logic"""
    
    def test_basic_processing(self):
        """Should process valid input correctly"""
        input_data = {'key': 'value'}
        result = process_data(input_data, {})
        assert result is not None

```

---

## Step 7: Generate References (if applicable)

### 7.1 Reference Document Creation

For each identified reference, create a markdown file with:

#### 7.1.1 Configuration Reference Template
**File**: `references/configuration.md`

```markdown
# Configuration Guide

## Environment Setup

### Prerequisites
- [Requirement 1]: Version X.Y+
- [Requirement 2]: Specific configuration needed

### Installation
\`\`\`bash
[Step-by-step installation instructions]
\`\`\`

### Environment Variables
| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `VAR_NAME` | Yes | What this variable does | `value` |
| `VAR_NAME_2` | No | Optional configuration | `default_value` |

### Configuration File Format
\`\`\`json
{
  "setting_1": "value",
  "setting_2": {
    "nested_setting": "value"
  }
}
\`\`\`

## Common Configurations

### Configuration 1: [Name]
[Description of when to use]
\`\`\`json
[Example configuration]
\`\`\`

### Configuration 2: [Name]
[Description of when to use]
\`\`\`json
[Example configuration]
\`\`\`
```

#### 7.1.2 API Schema Reference Template
**File**: `references/api-schema.md`

```markdown
# API Schema Documentation

## Overview
[Description of the API being documented]

## Authentication
[How to authenticate with the API]

## Endpoints

### GET /endpoint
**Purpose**: [What this endpoint does]

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param1` | string | Yes | [Description] |
| `param2` | integer | No | [Description] |

**Response**:
\`\`\`json
{
  "status": "success",
  "data": {
    "field1": "value",
    "field2": 123
  }
}
\`\`\`

**Error Response**:
\`\`\`json
{
  "status": "error",
  "code": 400,
  "message": "Invalid request"
}
\`\`\`

**Examples**:
\`\`\`bash
curl -X GET "https://api.example.com/endpoint?param1=value" \\
  -H "Authorization: Bearer TOKEN"
\`\`\`

### POST /endpoint
[Similar structure for POST endpoints]
```

#### 7.1.3 Troubleshooting Reference Template
**File**: `references/troubleshooting.md`

```markdown
# Troubleshooting Guide

## Common Errors

### Error: "[Error message]"
**Cause**: [What causes this error]
**Solution**: [Step-by-step solution]
**Prevention**: [How to avoid in future]

### Error: "[Another error message]"
**Cause**: [Root cause analysis]
**Solution**: [Detailed solution steps]
**Prevention**: [Prevention tips]

## Debug Mode
Enable debug logging to diagnose issues:
\`\`\`bash
python3 scripts/main.py --input data.txt --output result.txt --verbose
\`\`\`

This generates detailed logs in `script.log`.

## Performance Issues

### Issue: Slow Processing
**Symptoms**: [How to recognize this issue]
**Diagnosis**: [How to investigate]
**Solutions**: 
- [Solution 1]
- [Solution 2]

## FAQ

**Q**: [Frequently asked question]
**A**: [Detailed answer]

**Q**: [Another common question]
**A**: [Answer with examples]
```

#### 7.1.4 Integration Implementation Template
**File**: `references/integration-[service-name].md`

```markdown
# Integration: [Service Name]

## Overview
[What this integration does and why it's useful]

## Prerequisites
- [Service] account with [permission level] access
- API key or authentication credentials
- [Any other requirements]

## Setup Instructions

### Step 1: Create/Obtain Credentials
[Detailed instructions for getting API key, OAuth token, etc.]

### Step 2: Configure Environment
\`\`\`bash
export [SERVICE]_API_KEY="your_api_key_here"
export [SERVICE]_API_URL="https://api.example.com"
\`\`\`

Or in `config.json`:
\`\`\`json
{
  "service": {
    "api_key": "your_api_key",
    "api_url": "https://api.example.com"
  }
}
\`\`\`

## Usage Examples

### Example 1: [Common Use Case]
[Description of what this example does]

\`\`\`bash
python3 scripts/main.py --input data.txt --output result.txt --service [service-name]
\`\`\`

### Example 2: [Advanced Use Case]
[Description of advanced usage]

\`\`\`bash
python3 scripts/main.py --input data.txt --output result.txt --service [service-name] --config config.json
\`\`\`

## Rate Limiting
[Information about API rate limits]
- Requests per second: [number]
- Monthly limit: [number or unlimited]
- Retry strategy: [Exponential backoff implemented]

## Troubleshooting

### Issue: "Authentication failed"
**Solution**: Verify API key is correct and has proper permissions

### Issue: "Rate limit exceeded"
**Solution**: Reduce concurrency or implement request queuing

## Cost Considerations
[If applicable, information about costs/pricing]

## Support & Documentation
[Links to external service documentation]
```

### 7.2 Reference Quality Standards

For all references, ensure:
- [ ] Clear section headers and navigation
- [ ] Code examples are valid and tested
- [ ] Templated configuration can be copy-pasted and used immediately
- [ ] Cross-references to other files are explicit (e.g., "See `scripts/main.py` line 45")
- [ ] No ambiguous or assumed knowledge
- [ ] Include "Go back" or "See also" links for navigation

---

## Step 8: Generate Assets (if applicable)

### 8.1 Asset Creation

#### 8.1.1 Template Assets
**File**: `assets/templates/[template-name].[ext]`

```
Purpose: Provide starter templates that users can customize

Guidelines:
- Include placeholder markers: {{PLACEHOLDER_NAME}}
- Add comments explaining each section
- Provide at least one complete example
- Document template variables in reference file

Example: assets/templates/config-template.json

{
  "// Configuration Template": "Replace values below",
  "// Input file path": "Path to input data",
  "input_file": "{{INPUT_FILE_PATH}}",
  "// Output file path": "Where to write results",
  "output_file": "{{OUTPUT_FILE_PATH}}",
  "// Processing options": "Customize behavior here",
  "options": {
    "verbose": false,
    "max_retries": 3,
    "timeout_seconds": 300
  }
}
```

#### 8.1.2 Sample Data Assets
**File**: `assets/samples/[sample-name].[ext]`

```
Purpose: Provide minimal, realistic test data

Guidelines:
- Represent typical/common use cases
- Include edge cases if relevant
- Keep file size small (<1MB)
- Document what each sample demonstrates

Example: assets/samples/sample-input.json

{
  "name": "Example Record",
  "type": "sample",
  "created_at": "2024-01-15T10:30:00Z",
  "tags": ["test", "example"],
  "metadata": {
    "source": "manual",
    "validation": "passed"
  }
}
```

#### 8.1.3 Configuration Examples
**File**: `assets/config/[config-name].json`

```
Purpose: Provide complete, working configuration files

Guidelines:
- Each config demonstrates a specific use case
- Include comments explaining each setting
- Provide 2-3 common configurations (basic, advanced, edge-case)
- Document where/how to use each configuration

Example: assets/config/basic-config.json

{
  "name": "basic-setup",
  "description": "Minimal configuration for standard use",
  "settings": {
    "processing": {
      "mode": "standard",
      "parallel": false
    },
    "output": {
      "format": "json",
      "indent": 2
    }
  }
}
```

### 8.2 Asset Reference in SKILL.md

Document assets with clear usage instructions:

```markdown
## Assets & Templates

### Configuration Templates
Use `assets/config/basic-config.json` as a starting point:

\`\`\`bash
cp assets/config/basic-config.json my-config.json
# Edit my-config.json with your settings
python3 scripts/main.py --config my-config.json
\`\`\`

### Sample Data
Test the skill with provided sample data:

\`\`\`bash
python3 scripts/main.py --input assets/samples/sample-input.json \\
                       --output result.json
\`\`\`

### Document Templates
Customize templates in `assets/templates/` for your use case.
```

---

## Step 9: Create a Comprehensive Implementation Guide (skill-manifest.md)

### 9.1 Manifest Structure

The skill-manifest.md is a standalone, step-by-step guide that captures:
- Complete directory structure with all file paths
- Full content for every file (ready to copy-paste)
- Testing & validation results
- Integration recommendations
- Related skills analysis
- Iterative refinement guidance

### 9.2 Manifest Template

**File**: `skill-manifest.md`

```markdown
# Skill Creation Manifest: [Skill Name]

**Date**: [YYYY-MM-DD]
**Version**: 1.0.0
**Target AI**: OpenAI Codex

---

## 1. Design & Context Analysis

### 1.1 Skill Overview
[Comprehensive description of skill]

### 1.2 Skill Type
**Classification**: [Document Processing | API Integration | Workflow Automation | etc.]

### 1.3 Existing Skills Review
The following existing skills were consulted:
- **[Skill A]** ([brief description and relationship])
- **[Skill B]** ([brief description and relationship])

**Differentiation**: This skill differs by [specific differences that justify creation]

### 1.4 Integration Recommendations
The following integrations could enhance this skill:

#### Integration: [Service Name]
- **Purpose**: [How it enhances the skill]
- **Proposed Implementation**: [What would be added]
- **Implementation Effort**: [Low | Medium | High]
- **Configuration File**: See `references/integration-[name].md`

### 1.5 Success Criteria & Guard Rails

**Success Conditions**:
- [Specific, testable condition 1]
- [Specific, testable condition 2]
- [Specific, testable condition 3]

**Out of Scope**:
- [Task that is explicitly NOT handled]
- [Task that is explicitly NOT handled]

**Limitations**:
- [Known constraint 1]
- [Known constraint 2]

---

## 2. Directory Structure Setup

### 2.1 Create Directory Structure
Execute these commands to create the skill folder:

\`\`\`bash
mkdir -p skill-name/{scripts,references,assets/{templates,samples,config}}
cd skill-name
touch SKILL.md LICENSE.txt
\`\`\`

### 2.2 Resulting Structure
\`\`\`
skill-name/
├── SKILL.md                           # Main skill definition
├── LICENSE.txt                        # License information
├── scripts/
│   ├── main.py                       # Primary processing script
│   ├── helpers.py                    # Utility functions
│   └── validate.py                   # Input validation
├── references/
│   ├── configuration.md              # Configuration guide
│   ├── api-schema.md                 # API documentation
│   ├── troubleshooting.md            # Common issues & solutions
│   └── integration-[service].md      # Integration setup
└── assets/
    ├── templates/
    │   ├── config-template.json      # Configuration template
    │   └── output-template.md        # Output format template
    ├── samples/
    │   └── sample-input.json         # Test data
    └── config/
        ├── basic-config.json         # Basic configuration
        ├── advanced-config.json      # Advanced configuration
        └── edge-case-config.json     # Edge case configuration
\`\`\`

---

## 3. File Creation: SKILL.md

**File Path**: `skill-name/SKILL.md`

\`\`\`markdown
[COMPLETE SKILL.MD CONTENT HERE - see Step 5.2]
\`\`\`

---

## 4. File Creation: Scripts

### 4.1 Script: `scripts/main.py`

**File Path**: `skill-name/scripts/main.py`

\`\`\`python
[COMPLETE MAIN.PY CONTENT HERE - see Step 6.1.2]
\`\`\`

**Validation Results**:
- [x] Handles edge case: empty input
- [x] Handles edge case: missing file
- [x] Handles edge case: permission denied
- [x] Exit codes follow Unix conventions
- [x] Error messages are user-friendly
- [x] Logging implemented at appropriate levels
- [x] All exceptions caught and handled
- [x] No hardcoded credentials or paths

### 4.2 Script: `scripts/helpers.py`

**File Path**: `skill-name/scripts/helpers.py`

\`\`\`python
[COMPLETE HELPERS.PY CONTENT]
\`\`\`

### 4.3 Script: `scripts/validate.py`

**File Path**: `skill-name/scripts/validate.py`

\`\`\`python
[COMPLETE VALIDATE.PY CONTENT]
\`\`\`

---

## 5. File Creation: References

### 5.1 Reference: `references/configuration.md`

**File Path**: `skill-name/references/configuration.md`

\`\`\`markdown
[COMPLETE CONFIGURATION.MD CONTENT]
\`\`\`

### 5.2 Reference: `references/api-schema.md`

**File Path**: `skill-name/references/api-schema.md`

\`\`\`markdown
[COMPLETE API-SCHEMA.MD CONTENT]
\`\`\`

### 5.3 Reference: `references/troubleshooting.md`

**File Path**: `skill-name/references/troubleshooting.md`

\`\`\`markdown
[COMPLETE TROUBLESHOOTING.MD CONTENT]
\`\`\`

### 5.4 Reference: `references/integration-[service].md`

**File Path**: `skill-name/references/integration-[service].md`

\`\`\`markdown
[COMPLETE INTEGRATION DOCUMENTATION]
\`\`\`

---

## 6. File Creation: Assets

### 6.1 Template: `assets/templates/config-template.json`

**File Path**: `skill-name/assets/templates/config-template.json`

\`\`\`json
[COMPLETE TEMPLATE CONTENT]
\`\`\`

**Usage**: Copy this file to your working directory and customize the values.

### 6.2 Sample Data: `assets/samples/sample-input.json`

**File Path**: `skill-name/assets/samples/sample-input.json`

\`\`\`json
[COMPLETE SAMPLE DATA]
\`\`\`

**Purpose**: Demonstrates typical input data; use for testing and validation.

### 6.3 Config: `assets/config/basic-config.json`

**File Path**: `skill-name/assets/config/basic-config.json`

\`\`\`json
[COMPLETE BASIC CONFIGURATION]
\`\`\`

### 6.4 Config: `assets/config/advanced-config.json`

**File Path**: `skill-name/assets/config/advanced-config.json`

\`\`\`json
[COMPLETE ADVANCED CONFIGURATION]
\`\`\`

---

## 7. Testing & Validation Results

### 7.1 Static Code Analysis
- [x] No syntax errors in Python scripts
- [x] All imports are available and standard
- [x] Type hints present on functions
- [x] Docstrings complete and accurate
- [x] Exception handling comprehensive
- [x] No hardcoded secrets or credentials
- [x] Logging implemented at DEBUG, INFO, WARNING, ERROR levels

### 7.2 Functional Testing
**Test Input**: `assets/samples/sample-input.json`

\`\`\`bash
cd skill-name
python3 scripts/main.py --input assets/samples/sample-input.json \\
                       --output /tmp/test-output.json --verbose
\`\`\`

**Expected Output**: Valid JSON file at `/tmp/test-output.json`

**Results**:
- [x] Script exits with code 0 (success)
- [x] Output format matches specification
- [x] Logs written to script.log
- [x] No temporary files left behind
- [x] Appropriate error messages on failure

### 7.3 Edge Case Testing

| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Valid input | `assets/samples/sample-input.json` | Success, exit code 0 | ✅ |
| Missing file | `/nonexistent/file.json` | Error, exit code 2 | ✅ |
| Empty file | Empty file | Error, exit code 1 | ✅ |
| Permission denied | Read-only file | Error, exit code 2 | ✅ |
| Invalid JSON | Malformed JSON | Error, exit code 1 | ✅ |
| Large file | 500MB file | Success (>30 seconds) | ✅ |

### 7.4 Dependency Documentation

**Required Packages**:
\`\`\`
Python 3.8+
requests>=2.28.0
pydantic>=1.9.0
\`\`\`

**Installation**:
\`\`\`bash
cd skill-name
pip install -r requirements.txt
\`\`\`

**Tested With**:
- Python 3.10.5
- requests 2.31.0
- pydantic 2.0.1

---

## 8. Integration Recommendations (Detailed)

### Integration: [Service Name] - Proposed Implementation

**Rationale**: This integration enables [specific capability]

**Implementation Steps**:
1. Create `references/integration-[service].md` (see Step 5.4) ✅
2. Add authentication parameters to `scripts/main.py`:
   \`\`\`python
   parser.add_argument('--[service]-api-key', help='API key for [service]')
   \`\`\`
3. Implement service client in `scripts/helpers.py`
4. Add integration tests to verify API connectivity

**Configuration**: See `references/integration-[service].md` for setup instructions

**Cost Impact**: [Free tier / Paid / Usage-based]

---

## 9. Related Skills & Extensions

### Related Skill: [Existing Skill]
**Relationship**: This skill [complements | extends | uses] [existing skill]
**Recommended Workflow**: Use [existing skill] → use [new skill] for complete solution

**Can be Used Together**:
\`\`\`bash
# Process with existing skill first
python3 ../existing-skill/scripts/main.py --input raw-data.json --output processed.json

# Then use new skill
python3 scripts/main.py --input processed.json --output final-output.json
\`\`\`

### Extending This Skill

To add new functionality:

1. **Add new script** to `scripts/` following naming convention
   - Name: `scripts/[feature-name].py`
   - Include complete docstring and error handling
   - Test thoroughly before committing

2. **Update SKILL.md**:
   - Document new functionality in "Usage" section
   - Reference new script with examples
   - Keep file under 500 lines

3. **Add documentation** to `references/`:
   - If feature requires setup: create `references/[feature]-setup.md`
   - If feature is complex: create `references/[feature]-guide.md`

4. **Add test cases** to validate new functionality

---

## 10. Iterative Refinement Guide

### 10.1 Testing Loop

After creating the skill, test with various phrasings to ensure Codex correctly identifies and loads it:

**Test Prompts**:
- "Create a [skill-name] implementation"
- "I need to [use case description] using [skill-name]"
- "Help me [specific task] with [skill-name]"

**Success Indicator**: Claude/Codex immediately recognizes the skill and loads appropriate context

### 10.2 Refinement Process

If the skill is not being loaded correctly:

1. **DO NOT** modify prompts to Codex
2. **DO** refine SKILL.md instructions:
   - Clarify "When to use this skill"
   - Improve "Clear Success Criteria"
   - Strengthen "Guard Rails" (especially what NOT to do)
   - Add more specific examples to "Quick Start"

3. **Test again** with same prompts

### 10.3 Versioning & Updates

When updating the skill:

```yaml
# In SKILL.md frontmatter
version: 1.1.0
updated: 2024-XX-XX
changes:
  - Added [feature]
  - Fixed [issue]
  - Improved [documentation]
```

Update the change log in SKILL.md with each version.

---

## 11. Validation Checklist

Before deployment, verify:

### File Structure
- [ ] All directories created according to structure
- [ ] All files created in correct locations
- [ ] No extraneous files or directories

### SKILL.md
- [ ] Frontmatter is valid YAML
- [ ] Title and overview are clear
- [ ] Success criteria explicitly defined
- [ ] Guard rails clearly stated
- [ ] References to scripts, references, assets are accurate
- [ ] File is approximately 500 lines or less
- [ ] Examples are copy-pasteable and accurate

### Scripts
- [ ] All scripts execute without syntax errors
- [ ] Error handling comprehensive
- [ ] Exit codes follow Unix conventions (0=success)
- [ ] Logging implemented appropriately
- [ ] No hardcoded credentials or paths
- [ ] Tested with sample data successfully
- [ ] Edge cases handled (empty input, missing files, etc.)
- [ ] Dependencies documented in comments

### References
- [ ] Configuration guide complete with examples
- [ ] API schema accurate and up-to-date
- [ ] Troubleshooting covers common issues
- [ ] Integration documentation complete if applicable

### Assets
- [ ] Templates include placeholder markers
- [ ] Sample data is minimal but representative
- [ ] Config files are valid and tested
- [ ] All assets referenced in SKILL.md

### Testing
- [ ] All test cases pass (see section 7.2-7.3)
- [ ] Documentation matches actual behavior
- [ ] Error messages are user-friendly
- [ ] Performance meets expectations

---

## 12. Next Steps

1. **Create the skill directory and files** following the structure in section 2
2. **Copy content** from sections 3-6 into corresponding files
3. **Test the skill** with the test cases in section 7
4. **Refine SKILL.md** if Codex doesn't load the skill correctly
5. **Package the skill** using the skill-creator tool when ready for distribution
6. **Monitor and iterate** based on user feedback using the refinement guide (section 10)

---

## Appendix: File Reference Quick Links

- **SKILL.md**: Section 3
- **scripts/main.py**: Section 4.1
- **scripts/helpers.py**: Section 4.2
- **scripts/validate.py**: Section 4.3
- **references/configuration.md**: Section 5.1
- **references/api-schema.md**: Section 5.2
- **references/troubleshooting.md**: Section 5.3
- **references/integration-[service].md**: Section 5.4
- **assets/templates/config-template.json**: Section 6.1
- **assets/samples/sample-input.json**: Section 6.2
- **assets/config/basic-config.json**: Section 6.3
- **assets/config/advanced-config.json**: Section 6.4

---

**End of Skill Creation Manifest**
```

---

## Step 10: Implementation Workflow for Codex

### 10.1 How to Use This Document with Codex

1. **Gather Input** (Step 1): Provide skill name and description
2. **Analyze Requirements** (Step 2): Codex determines skill type and needed resources
3. **Review Best Practices** (Step 3): Codex applies design principles from how-to-build-claude-skills.md
4. **Design Structure** (Step 4): Codex plans directory layout
5. **Generate SKILL.md** (Step 5): Codex creates main skill definition
6. **Generate Scripts** (Step 6): Codex creates production-ready scripts with testing
7. **Generate References** (Step 7): Codex creates documentation and guides
8. **Generate Assets** (Step 8): Codex creates templates and sample data
9. **Create Manifest** (Step 9): Codex generates complete skill-manifest.md
10. **Output**: User receives complete skill-manifest.md ready for implementation

### 10.2 Codex Optimization Considerations

**Prompt Structure for Codex**:
```
Create a Claude skill with the following requirements:
- Name: [skill-name]
- Description: [what it does]
- Primary use case: [use case]

Follow the 10-step skill creation process:
1. Gather input (DONE)
2. Analyze requirements
3. Consult best practices
4. Design structure
5. Generate SKILL.md
6. Generate production-ready scripts with comprehensive testing
7. Generate reference documentation
8. Generate assets and templates
9. Create a complete skill-manifest.md
10. Output the manifest with all file contents ready to copy-paste

For each script:
- Include comprehensive error handling
- Document all functions
- Add logging at appropriate levels
- Provide test cases
- Validate before delivery
```

**Codex will then**:
- Generate all files according to specifications
- Include testing & validation for each script
- Create comprehensive references
- Output complete skill-manifest.md with all content ready to copy-paste

---

## Summary of Key Improvements

| Area | Improvement |
|------|-------------|
| **Script Quality** | Added comprehensive error handling, logging, type hints, exit codes, and pre-delivery testing checklist |
| **Testing & Validation** | Added 6 explicit validation steps with test cases, edge case handling, and integration testing |
| **Documentation** | Added template-based references for configuration, APIs, troubleshooting, and integrations |
| **Manifest Structure** | Expanded manifest to include validation results, testing evidence, and iterative refinement guidance |
| **Codex Optimization** | Added Codex-specific prompting structure and workflow considerations |
| **Dependency Management** | Added explicit requirements documentation and version tracking |
| **Progressive Disclosure** | Added clear guidance on keeping SKILL.md lean while moving detail to references |
| **Integration Support** | Added detailed integration recommendation templates and proposed implementation guidance |
| **Iterative Refinement** | Added comprehensive testing loop and refinement process for continuous improvement |

This improved version provides Codex with specific, actionable guidance for creating robust, well-tested, production-ready Claude skills with comprehensive documentation and validation.