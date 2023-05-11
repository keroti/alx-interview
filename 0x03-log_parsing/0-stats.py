#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """Print the metrics"""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


def parse_line(line):
    """Parse a log line and return the file size and status code"""
    fields = line.split()
    if len(fields) < 7:
        return None, None
    try:
        file_size = int(fields[6])
        status_code = int(fields[8])
    except (ValueError, IndexError):
        return None, None
    return file_size, status_code


# Initialize variables
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Read lines from stdin
for line in sys.stdin:
    # Parse the line
    file_size, status_code = parse_line(line)
    if file_size is None or status_code is None:
        continue

    # Update metrics
    file_size += file_size
    status_codes[status_code] += 1
    line_count += 1

    # Print stats every 10 lines or when interrupted
    if line_count % 10 == 0:
        print_stats(file_size, status_codes)

# Print final stats
print_stats(file_size, status_codes)
