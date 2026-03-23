#!/usr/bin/env python3
"""
Date conversion utility script.

This script provides functions to convert between different date formats and timezones.
"""

import argparse
from datetime import datetime
import pytz
from dateutil import parser

def parse_date(date_str, input_fmt=None, timezone='UTC'):
    """
    Parse a date string into a datetime object.
    
    Args:
        date_str (str): The date string to parse
        input_fmt (str, optional): Format string (strptime format). If None, uses dateutil.parser
        timezone (str): Timezone for the output datetime (default: 'UTC')
        
    Returns:
        datetime: Datetime object in the specified timezone
    """
    tz = pytz.timezone(timezone)
    
    if input_fmt:
        dt = datetime.strptime(date_str, input_fmt)
    else:
        dt = parser.parse(date_str)
    
    # If the datetime is naive, localize it
    if dt.tzinfo is None:
        dt = tz.localize(dt)
    
    return dt.astimezone(tz)

def format_date(dt, output_fmt='%Y-%m-%d %H:%M:%S %Z'):
    """
    Format a datetime object as a string.
    
    Args:
        dt (datetime): Datetime object to format
        output_fmt (str): Format string (strftime format)
        
    Returns:
        str: Formatted date string
    """
    return dt.strftime(output_fmt)

def convert_timezone(dt, target_timezone):
    """
    Convert a datetime to a different timezone.
    
    Args:
        dt (datetime): Source datetime
        target_timezone (str): Target timezone (e.g., 'Asia/Singapore', 'US/Eastern')
        
    Returns:
        datetime: Datetime in the target timezone
    """
    target_tz = pytz.timezone(target_timezone)
    return dt.astimezone(target_tz)

def main():
    parser = argparse.ArgumentParser(description='Convert between date formats and timezones')
    
    # Input options
    parser.add_argument('date', nargs='?', help='Date string to convert (omit to use current time)')
    parser.add_argument('--input-format', '-i', help='Input date format (strptime format)')
    
    # Output options
    parser.add_argument('--output-format', '-o', default='%Y-%m-%d %H:%M:%S %Z',
                      help='Output date format (strftime format)')
    parser.add_argument('--input-tz', default='UTC',
                      help='Input timezone (default: UTC)')
    parser.add_argument('--output-tz', help='Output timezone (e.g., Asia/Singapore)')
    
    # List timezones
    parser.add_argument('--list-timezones', action='store_true',
                      help='List all available timezones')
    
    args = parser.parse_args()
    
    if args.list_timezones:
        print("Available timezones:")
        for tz in pytz.all_timezones:
            print(f"  {tz}")
        return
    
    try:
        # Parse input date or use current time
        if args.date:
            dt = parse_date(args.date, args.input_format, args.input_tz)
        else:
            dt = datetime.now(pytz.timezone(args.input_tz))
        
        # Convert timezone if requested
        if args.output_tz:
            dt = convert_timezone(dt, args.output_tz)
        
        # Format and print the result
        print(format_date(dt, args.output_format))
        
    except ValueError as e:
        print(f"Error: {e}")
        print("\nExamples of usage:")
        print("  Convert specific date: convert_date.py '2023-11-02 15:30:00' --input-tz 'UTC' --output-tz 'Asia/Singapore'")
        print("  Format output: convert_date.py '2023-11-02' --input-format '%Y-%m-%d' --output-format '%d %B %Y'")
        print("  List timezones: convert_date.py --list-timezones")

if __name__ == "__main__":
    main()
