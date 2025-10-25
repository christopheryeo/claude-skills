---
name: search-calendar
description: >-
  Search Google Calendar with natural language. Find events by date, title, attendees, or email domains.
  
  Parameters:
  - date (string): 'tomorrow', 'next Monday', 'Oct 25'
  - time_range: {start: ISO datetime, end: ISO datetime}
  - subject (string): Search in event titles
  - attendees (string[]): Filter by attendee names
  - emails (string[]): Filter by email/domains
  
  Returns: [{
    event_id: string,
    title: string,
    start_time: ISO datetime,
    end_time: ISO datetime,
    attendees: {name: string, email: string, response_status: string}[],
    location?: string,
    description?: string
  }]
---

# Search Calendar Skill

This skill teaches Claude how to intelligently search your Google Calendar with multiple search criteria and flexible natural language understanding.

## When to Use This Skill

Use this skill when users ask questions like:
- "Show me events on Monday with Eddie"
- "Find all 'SnR:Huddle' meetings this week"
- "What do I have on 21 Oct 2025?"
- "List standup meetings with John Hor next week"
- "Events with sentient.io emails today"
- "When am I meeting with Wilson Ang?"

## How to Search Calendars Effectively

### Search Dimensions

Claude can search calendars across these dimensions:

#### 1. **By Day** (Today, Tomorrow, Specific Weekdays)
- "today", "tomorrow", "yesterday"
- Weekday names: "Monday", "Tuesday", etc.
- With modifiers: "next Monday", "last Friday", "this Thursday"

#### 2. **By Date** (Specific Dates)
- Multiple formats supported: "21 Oct 2025", "October 21", "2025-10-21", "21/10/2025"
- Claude can parse these flexibly

#### 3. **By Week** (Calendar Weeks)
- "this week", "next week", "last week"

#### 4. **By Subject/Title** (Event Names)
- Search event titles: "SnR:Huddle", "standup", "planning", "review"
- Use partial matches: "huddle" finds "SnR:Huddle"

#### 5. **By Attendee Name** (People Invited)
- Search by name: "Eddie", "Wilson Ang", "John Hor"
- Use first name, last name, or abbreviations: "Ed" finds "Eddie"
- Names are fuzzy-matched to handle variations

#### 6. **By Email Address** (Attendee Emails)
- Full or partial emails: "eddie@sentient.io", "sentient.io", "mani@"
- Searches attendee email list

### Combining Criteria (AND Logic)

Combine multiple search dimensions to narrow results:
- Date + Attendee: "Show me events with Eddie on Monday"
- Subject + Week: "Find all 'standup' meetings this week"
- Subject + Attendee + Date: "'SnR:Huddle' with John on Friday"
- Multiple attendees: "Events with Eddie and Mani next week"

### Implementation Strategy

When searching calendars, Claude should:

1. **Parse the user query** to identify:
   - Time reference (day, date, week)
   - Subject/keywords
   - Attendee names or emails

2. **Use Google Calendar tools** to:
   - Get list of calendars accessible
   - Retrieve events for the identified time range
   - Filter by subject, attendees, and other criteria

3. **Format results** with:
   - Event title and time
   - Location
   - Attendee list with their email addresses
   - Link to the calendar event
   - Any relevant description

4. **Apply filtering logic**:
   - Exclude cancelled events
   - Include all other event statuses (accepted, tentative, needs action, declined)
   - Limit to 50 most recent results
   - Sort by date (newest first)

### Natural Language Processing

Claude should understand:
- Flexible phrasing: "What's on my calendar?" vs "Show me my events"
- Fuzzy matching: "Wil" for "Wilson", "Ed" for "Eddie"
- Multiple date formats naturally
- Partial information: "meetings with sentient.io" or just "Eddie" without full context
- Relative time references: "this week", "next Monday", "last Friday"

## Examples

### Example 1: Today's Events
**User:** "Show me my calendar for today"

**Claude should:**
1. Get current date
2. Retrieve events for today from all accessible calendars
3. Format and display them

### Example 2: Events with Specific Person
**User:** "Find all meetings with Eddie this week"

**Claude should:**
1. Identify time range: this week (Monday-Sunday)
2. Query all calendars for events in that range
3. Filter for events where "Eddie" is an attendee (fuzzy match on attendee names)
4. Return matching events with full details

### Example 3: Subject + Attendee + Date
**User:** "Show me 'SnR:Huddle' meetings with John Hor next week"

**Claude should:**
1. Identify time range: next week
2. Query calendars for events with "Huddle" or "SnR" in title
3. Filter for events where "John Hor" is invited
4. Return combined results

### Example 4: Email-based Search
**User:** "What meetings do I have with people from sentient.io?"

**Claude should:**
1. Query recent events (default: next 30 days)
2. Filter for events with attendees having @sentient.io email
3. Return matching events

## Important Guidelines

### Timezone Handling
- Results should be displayed in Singapore Time (SGT / UTC+8)
- If user is in different timezone, convert display times appropriately

### Time Ranges
- **Day-based search**: Search that specific 24-hour period
- **Week-based search**: Search Monday through Sunday of that calendar week
- **Date-based search**: Search that specific date
- **No time specified**: Default to next 30 days for open searches

### Attendee Matching
- Use fuzzy matching for names (70% similarity threshold)
- Handle partial names and nicknames
- For emails: support partial matches (e.g., "eddie@" matches "eddie@sentient.io")
- Match against all visible attendees, not just organizer

### Event Status
- **Always exclude**: Cancelled events
- **Always include**: All other statuses (Accepted, Tentative, Declined, Needs Action)
- Display attendee RSVP status when listing events

### Result Limits
- Return maximum 50 events per search
- Show newest/most recent first
- Include full details: title, time, location, attendees, calendar link

## Tips for Better Results

1. **Be specific**: Include attendee names or subjects when possible to narrow results
2. **Use natural dates**: "next Monday" works better than calculating dates manually
3. **Combine criteria**: Rather than "all my meetings with Eddie", use "Eddie next week" for faster results
4. **Verify attendee names**: If unsure of spelling, use nicknames - fuzzy matching handles it

## Handling Edge Cases

**Multiple people with similar names:**
- Display all matches and ask user to clarify if needed
- Show email addresses to help distinguish

**Events without attendees:**
- Include in results when subject matches
- Mark "No attendees" or "Private" if applicable

**All-day events:**
- Include in results
- Display as "All day" rather than specific times

**Recurring events:**
- Return individual instances for the date range queried
- Show the full series context if available

**No results:**
- Explain why no events were found
- Suggest broadening the search (e.g., "try searching all week instead of just Monday")

## Integration with Other Tools

This skill works with Claude's existing calendar tools and can be combined with:
- Email searches (find emails about specific meetings)
- Document creation (create notes about meetings)
- Task management (create tasks from meeting discussions)

## Security and Privacy

- Search only calendars the user has read access to
- Don't expose private event details beyond what the user authorized
- Respect calendar sharing permissions
- Only display information the user can see

## Troubleshooting

**"No calendars found"**
- User may need to grant calendar access
- Verify Google Calendar permissions

**"No events matching"**
- Try broader search terms
- Check spelling of names/subjects
- Extend date range

**"Wrong person matched"**
- For ambiguous names, ask user to clarify
- Use email addresses for specific identification
- Provide full names in results to avoid confusion

---

## Quick Start for Claude

When a user asks about their calendar:

1. Parse their request for: **time** (when), **subject** (what), **people** (who)
2. Use calendar tools to fetch events
3. Filter intelligently based on all criteria provided
4. Format results clearly with event details and links
5. For unclear queries, ask clarifying questions

The skill is designed to be conversational - Claude should handle natural language calendar queries without requiring specific syntax or complex instructions from the user.