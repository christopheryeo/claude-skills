# Search Calendar Skill - Claude Skills Edition

This is a **proper Claude Skill** built according to Anthropic's Agent Skills specifications.

## What This Skill Does

This skill teaches Claude how to search your Google Calendar intelligently across multiple dimensions:
- By day (today, tomorrow, Monday, etc.)
- By date (21 Oct 2025, 2025-10-21, etc.)
- By week (this week, next week, last week)
- By subject/event title
- By attendee names (with fuzzy matching)
- By email addresses

## Structure

This skill follows Anthropic's specifications:
```
search-calendar/
├── SKILL.md                    # Main skill file with instructions
├── search_calendar_helper.py   # Reference helper script
└── README.md                   # This file
```

## How It Works

According to Anthropic's Agent Skills design:

1. **SKILL.md** contains:
   - YAML frontmatter with `name` and `description`
   - Instructions for Claude on how to search calendars
   - Examples of search queries
   - Guidelines for combining search criteria
   - Tips for better results

2. **Progressive Disclosure**:
   - Claude loads the skill metadata (name, description) first
   - When a calendar search is relevant, Claude reads the full SKILL.md
   - Claude uses built-in calendar tools to execute the search
   - Only necessary context is loaded into Claude's context window

3. **Composable**:
   - This skill can work with other skills (document creation, task management, etc.)
   - Multiple search criteria work together seamlessly

## Using This Skill

### With Claude.ai
1. Place the `search-calendar` folder in your Claude skills directory
2. Enable the skill in Claude settings
3. Ask Claude calendar questions naturally:
   - "Show me events on Monday with Eddie"
   - "Find all 'SnR:Huddle' meetings this week"
   - "What meetings do I have with sentient.io?"

### With Claude API
1. Upload the skill via the Claude API
2. Reference it when making requests
3. Claude will automatically use it for calendar queries

### With Claude Code
1. Install the skill as a plugin
2. Ask Claude Code to search your calendar
3. Claude Code will load and use the skill instructions

## Key Design Principles

### 1. Progressive Disclosure
The skill only loads context as needed:
- **First level**: Metadata (name, description) - 2-3 tokens
- **Second level**: Full SKILL.md when calendar query detected - ~2000 tokens
- **Third level**: Helper scripts only when Claude needs to execute searches

### 2. Composability
This skill works with:
- Built-in Google Calendar tools (via Zapier)
- Other Claude skills for document creation
- Email searching skills for related emails
- Task management skills

### 3. Executable Code
The `search_calendar_helper.py` script:
- Demonstrates parsing logic for natural language
- Shows fuzzy matching implementation
- Guides Claude on how to use calendar tools
- Can be executed to show search parameters

## Implementation Details

### Search Parsing
The skill teaches Claude to parse:
- **Time references**: today, tomorrow, Monday, next week, specific dates
- **Subject keywords**: Event titles and partial matches
- **Attendee names**: First names, last names, nicknames (fuzzy matched)
- **Emails**: Full or partial email addresses

### Filtering Logic
Events are filtered by:
- Time range (day/date/week)
- Subject/title matching
- Attendee presence (by name or email)
- Event status (exclude cancelled, include all others)

### Result Formatting
Results include:
- Event title and time (Singapore Time)
- Location
- Full attendee list with RSVP status
- Direct Google Calendar link

## Example Conversations

### Example 1
**User**: "Show me my meetings with Eddie next week"

Claude will:
1. Recognize this is a calendar search
2. Load the search-calendar skill
3. Parse: time="next week", attendee="Eddie"
4. Use calendar tools to get events
5. Filter for "Eddie" in attendees
6. Return formatted results

### Example 2
**User**: "Find all standup meetings this week with John"

Claude will:
1. Parse: time="this week", subject="standup", attendee="John"
2. Query calendars for the week
3. Filter by "standup" in title
4. Filter by "John" in attendees
5. Return matching events

## Integration with Calendar Tools

Claude has built-in access to calendar tools via Zapier:
- `list_gcal_calendars` - Get all accessible calendars
- `list_gcal_events` - Retrieve events for a date range
- `fetch_gcal_event` - Get details of a specific event

The skill teaches Claude how to use these tools effectively based on the search criteria.

## Limitations

- Results limited to 50 events per search
- Searches visible calendars only
- Cancelled events excluded by design
- Time zone fixed to Singapore Time (SGT)
- Fuzzy matching uses 70% similarity threshold

## Why This Design?

This proper Claude Skill design is better than a standalone application because:

1. **Efficient**: Uses progressive disclosure - loads only needed context
2. **Composable**: Works with other skills automatically
3. **Simple**: Clear instructions for Claude to follow
4. **Scalable**: Context window usage scales with task complexity, not skill complexity
5. **Maintainable**: Single SKILL.md file is easier to update than complex code
6. **Portable**: Can be used with Claude API, Claude Code, or Claude.ai

## Comparison to Earlier Version

The earlier implementation was a standalone Python application that tried to:
- Handle all authentication
- Execute all search logic
- Manage state and configuration
- Provide its own output formatting

This proper implementation instead:
- Teaches Claude how to search (instructions)
- Provides reference code Claude can learn from
- Lets Claude use existing calendar tools
- Lets Claude handle output formatting naturally

This is the Anthropic-recommended pattern for skills.

## Getting Started

1. Place the `search-calendar` folder in `/mnt/skills/user/`
2. Enable it in Claude settings
3. Start asking Claude calendar questions naturally
4. Claude will automatically recognize when to use this skill

## File Details

### SKILL.md
- Contains YAML frontmatter: name and description
- ~250 lines of instructions and guidelines
- Examples of different search types
- Integration guidance
- Troubleshooting tips

### search_calendar_helper.py
- ~150 lines of Python reference code
- Shows how to parse natural language
- Demonstrates fuzzy matching
- Guides calendar tool usage
- Can be executed to show parsed criteria

### README.md
- This file
- Explains skill structure and design
- Usage examples
- Integration details

## Questions?

Refer to the [Agent Skills documentation](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) for more information on how Claude Skills work.

---

**This is a proper Claude Skill** ✅

Built according to Anthropic's Agent Skills specifications for:
- Progressive disclosure
- Composability  
- Efficiency
- Simplicity
```

Perfect! That's all three files. Now you have everything you need for your Claude Skill:

📁 **Your complete skill folder:**
```
search-calendar/
├── SKILL.md                    # File 1 - The core skill
├── search_calendar_helper.py   # File 2 - Helper script
└── README.md                   # File 3 - Documentation