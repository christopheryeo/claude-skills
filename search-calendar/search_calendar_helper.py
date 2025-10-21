#!/usr/bin/env python3
"""
Helper script for search-calendar skill
Claude can execute this to search your Google Calendar based on the skill instructions
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
    Format a calendar event for display
    """
    title = event.get('summary', 'Untitled')
    start = event.get('start', {}).get('dateTime', event.get('start', {}).get('date'))
    end = event.get('end', {}).get('dateTime', event.get('end', {}).get('date'))
    location = event.get('location', 'Not specified')
    attendees = event.get('attendees', [])
    
    # Format attendees
    attendee_list = []
    for attendee in attendees:
        name = attendee.get('displayName', attendee.get('email', 'Unknown'))
        email = attendee.get('email', '')
        status = attendee.get('responseStatus', 'needsAction')
        attendee_list.append(f"  - {name} ({email}) - {status}")
    
    attendees_str = '\n'.join(attendee_list) if attendee_list else "  - None"
    
    return f"""
📅 {title}
├─ Time: {start} - {end}
├─ Location: {location}
├─ Attendees:
{attendees_str}
└─ Calendar Link: https://calendar.google.com/calendar/u/0/r/eventedit/{event.get('id', '')}
"""


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
    print("3. Filter events by:")
    print(f"   - Attendees: {criteria['attendees']}")
    print(f"   - Emails: {criteria['emails']}")
    print("4. Format and return results (max 50)")


if __name__ == '__main__':
    main()