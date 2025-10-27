#!/usr/bin/env python3
"""
Helper script for search-calendar skill
Claude can execute this to search your Google Calendar based on the skill instructions

OPTIMIZED FOR TIME-BASED BRIEFINGS:
- Returns explicit start/end times in Asia/Singapore timezone
- Calculates event duration
- Identifies events needing prep time
- Extracts full descriptions and attendee context
- Ensures timestamp consistency for briefing integration
"""

import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# This script serves as a reference for how to search calendars
# Claude will use the built-in calendar tools (via Zapier) to:
# 1. Get all accessible calendars
# 2. Retrieve events for specified date ranges
# 3. Filter by subject, attendees, emails
# 4. Format and return results

def parse_time_reference(query):
    """
    Parse time references from user query.
    Returns: (start_date, end_date, description)
    """
    query_lower = query.lower()
    today = datetime.now(ZoneInfo('Asia/Singapore'))
    
    # Today
    if 'today' in query_lower:
        return (today.replace(hour=0, minute=0, second=0, microsecond=0),
                today.replace(hour=23, minute=59, second=59, microsecond=999999),
                "today")
    
    # Tomorrow
    if 'tomorrow' in query_lower:
        tomorrow = today + timedelta(days=1)
        return (tomorrow.replace(hour=0, minute=0, second=0, microsecond=0),
                tomorrow.replace(hour=23, minute=59, second=59, microsecond=999999),
                "tomorrow")
    
    # Yesterday
    if 'yesterday' in query_lower:
        yesterday = today - timedelta(days=1)
        return (yesterday.replace(hour=0, minute=0, second=0, microsecond=0),
                yesterday.replace(hour=23, minute=59, second=59, microsecond=999999),
                "yesterday")
    
    # This week
    if 'this week' in query_lower:
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
        return (monday.replace(hour=0, minute=0, second=0, microsecond=0), sunday, "this week")
    
    # Next week
    if 'next week' in query_lower:
        monday = today - timedelta(days=today.weekday()) + timedelta(weeks=1)
        sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
        return (monday.replace(hour=0, minute=0, second=0, microsecond=0), sunday, "next week")
    
    # Last week
    if 'last week' in query_lower:
        monday = today - timedelta(days=today.weekday()) - timedelta(weeks=1)
        sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
        return (monday.replace(hour=0, minute=0, second=0, microsecond=0), sunday, "last week")
    
    # Default: next 30 days
    return (today, today + timedelta(days=30), "next 30 days")


def fuzzy_match(text, pattern, threshold=70):
    """
    Simple fuzzy matching for attendee/subject matching
    Returns True if pattern matches text with sufficient similarity
    """
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    
    # Exact match
    if pattern_lower in text_lower:
        return True
    
    # Partial word match
    words = text_lower.split()
    for word in words:
        if pattern_lower == word[:len(pattern_lower)]:
            return True
    
    return False


def calculate_duration(start, end):
    """
    Calculate event duration in minutes.
    Handles both datetime and date-only events.
    Returns duration in minutes, or None for all-day events.
    """
    try:
        if isinstance(start, str):
            start = datetime.fromisoformat(start.replace('Z', '+00:00'))
        if isinstance(end, str):
            end = datetime.fromisoformat(end.replace('Z', '+00:00'))
        
        duration = (end - start).total_seconds() / 60
        return int(duration)
    except:
        return None


def needs_prep_time(event):
    """
    Determine if an event needs prep time based on:
    - Presence of Drive links in description
    - Number of attendees (>5)
    - Presence of attachments or conference data
    - Keywords suggesting prep needed (agenda, review, presentation)
    
    Returns: boolean
    """
    prep_needed = False
    
    # Check description for Drive links
    description = event.get('description', '')
    if description:
        drive_indicators = [
            'docs.google.com/document',
            'docs.google.com/spreadsheets',
            'docs.google.com/presentation',
            'drive.google.com',
            'agenda',
            'review',
            'presentation',
            'proposal',
            'deck'
        ]
        if any(indicator in description.lower() for indicator in drive_indicators):
            prep_needed = True
    
    # Check attendee count
    attendees = event.get('attendees', [])
    if len(attendees) > 5:
        prep_needed = True
    
    # Check for attachments or conference data
    if event.get('attachments') or event.get('conferenceData'):
        prep_needed = True
    
    return prep_needed


def extract_conference_link(event):
    """
    Extract video conference link from event.
    Returns: {type: string, url: string} or None
    """
    conference_data = event.get('conferenceData')
    if conference_data:
        entry_points = conference_data.get('entryPoints', [])
        for entry in entry_points:
            if entry.get('entryPointType') == 'video':
                return {
                    'type': conference_data.get('conferenceSolution', {}).get('name', 'Video Call'),
                    'url': entry.get('uri', '')
                }
    
    # Fallback: check description for common video conference links
    description = event.get('description', '')
    if 'meet.google.com' in description:
        import re
        match = re.search(r'https://meet\.google\.com/[a-z\-]+', description)
        if match:
            return {'type': 'Google Meet', 'url': match.group(0)}
    if 'zoom.us' in description:
        import re
        match = re.search(r'https://[a-z0-9\-]+\.zoom\.us/j/\d+', description)
        if match:
            return {'type': 'Zoom', 'url': match.group(0)}
    
    return None


def extract_criteria(query):
    """
    Extract search criteria from user query
    Returns: dict with 'time_range', 'subject', 'attendees', 'emails'
    """
    criteria = {
        'time_range': parse_time_reference(query),
        'subject': [],
        'attendees': [],
        'emails': []
    }
    
    # Extract emails
    import re
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, query)
    criteria['emails'] = emails
    
    # Remove emails from query for further processing
    query_clean = re.sub(email_pattern, '', query)
    
    # Common names (for demonstration - could be expanded)
    common_names = ['eddie', 'wilson', 'john', 'mani', 'ang', 'hor']
    for name in common_names:
        if name.lower() in query_clean.lower():
            criteria['attendees'].append(name)
    
    return criteria


def format_event(event):
    """
    Format a calendar event for display with enriched data for briefings.
    Returns event with explicit timestamps, duration, prep indicator, and full context.
    """
    title = event.get('summary', 'Untitled')
    
    # Get times and ensure they're in Asia/Singapore timezone
    start_raw = event.get('start', {}).get('dateTime', event.get('start', {}).get('date'))
    end_raw = event.get('end', {}).get('dateTime', event.get('end', {}).get('date'))
    
    # Parse and convert to Singapore timezone
    sgt = ZoneInfo('Asia/Singapore')
    if start_raw and end_raw:
        try:
            start_dt = datetime.fromisoformat(start_raw.replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(end_raw.replace('Z', '+00:00'))
            
            # Convert to Singapore time
            start_sgt = start_dt.astimezone(sgt)
            end_sgt = end_dt.astimezone(sgt)
            
            start = start_sgt.isoformat()
            end = end_sgt.isoformat()
            duration = calculate_duration(start_sgt, end_sgt)
        except:
            start = start_raw
            end = end_raw
            duration = None
    else:
        start = start_raw or "Not specified"
        end = end_raw or "Not specified"
        duration = None
    
    location = event.get('location', 'Not specified')
    description = event.get('description', '')
    attendees = event.get('attendees', [])
    
    # Calculate prep needed
    prep_needed = needs_prep_time(event)
    
    # Extract conference link
    conference = extract_conference_link(event)
    
    # Format attendees with full context
    attendee_list = []
    for attendee in attendees:
        name = attendee.get('displayName', attendee.get('email', 'Unknown'))
        email = attendee.get('email', '')
        status = attendee.get('responseStatus', 'needsAction')
        attendee_list.append(f"  - {name} ({email}) - {status}")
    
    attendees_str = '\n'.join(attendee_list) if attendee_list else "  - None"
    
    # Build enriched output
    output = f"""
📅 {title}
├─ Time: {start} → {end}"""
    
    if duration:
        output += f"\n├─ Duration: {duration} minutes"
    
    output += f"""
├─ Location: {location}
├─ Attendees ({len(attendees)}):
{attendees_str}"""
    
    if prep_needed:
        output += "\n├─ ⚠️  Prep Time Needed"
    
    if conference:
        output += f"\n├─ Conference: {conference['type']} - {conference['url']}"
    
    if description:
        output += f"\n├─ Description:\n{description[:200]}{'...' if len(description) > 200 else ''}"
    
    output += f"\n└─ Calendar Link: https://calendar.google.com/calendar/u/0/r/eventedit/{event.get('id', '')}"
    
    return output


def main():
    """
    Main entry point - can be called by Claude
    """
    if len(sys.argv) < 2:
        print("Usage: python search_calendar_helper.py '<search query>'")
        print("Example: python search_calendar_helper.py 'Show me events with Eddie on Monday'")
        return
    
    query = ' '.join(sys.argv[1:])
    
    # Parse the query
    criteria = extract_criteria(query)
    time_range = criteria['time_range']
    
    print(f"\nSearching for: {query}")
    print(f"Time range: {time_range[2]}")
    print(f"Criteria: Attendees={criteria['attendees']}, Emails={criteria['emails']}")
    print("\nTo complete the search, Claude will:")
    print("1. Get all accessible calendars using list_gcal_calendars")
    print("2. Query events using list_gcal_events with date range:", time_range[0], "to", time_range[1])
    print("3. For each event, enrich with:")
    print("   - Explicit start/end times in Asia/Singapore timezone (ISO 8601)")
    print("   - Duration in minutes")
    print("   - Prep time indicator (Drive links, >5 attendees, attachments)")
    print("   - Full description and attendee context")
    print("   - Conference links (Meet, Zoom, Teams)")
    print("4. Filter events by:")
    print(f"   - Attendees: {criteria['attendees']}")
    print(f"   - Emails: {criteria['emails']}")
    print("5. Sort chronologically and return results (max 50)")
    print("\nTIMEZONE: All timestamps will be in Asia/Singapore (SGT/UTC+8)")
    print("BRIEFING INTEGRATION: Results optimized for time-based briefing correlation")


if __name__ == '__main__':
    main()