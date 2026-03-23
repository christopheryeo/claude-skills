#!/usr/bin/env python3
"""
Convert dates to reverse month format (YYYY-MM).

This script takes a date in various formats and converts it to
"reverse month" format (YYYY-MM), which is the ISO date format
with only the year and month components.
"""

import sys
from dateutil import parser

def convert_to_reverse_month(date_string):
    """
    Convert a date string to reverse month format (YYYY-MM).
    
    Args:
        date_string: A date string in any common format
        
    Returns:
        A string in YYYY-MM format
    """
    try:
        parsed_date = parser.parse(date_string)
        return parsed_date.strftime('%Y-%m')
    except Exception as e:
        return f"Error: Unable to parse date: '{date_string}'. Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_month.py <date_string>")
        print("Example: python convert_month.py '21 Oct 2025'")
        sys.exit(1)
    
    date_string = sys.argv[1]
    result = convert_to_reverse_month(date_string)
    print(result)
```