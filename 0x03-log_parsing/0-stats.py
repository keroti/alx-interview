#!/usr/bin/python3
"""Log Parsing function"""

import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
status_count = {code: 0 for code in status_codes}
size = 0
line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        code = parts[-2]
        size = int(parts[-1])
        if code in status_codes:
            status_count[code] += 1
        size += size
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(size))
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print("{}: {}".format(code, status_count[code]))
    except Exception:
        pass


def print_metrics(code, size):
    """Print Metrics of Total file size & Status Code count."""
    print("File size: {:d}".format(size))
    for i in sorted(code.keys()):
        if status_count[i] > 0:
            print("{}: {:d}".format(i, status_count[i]))
