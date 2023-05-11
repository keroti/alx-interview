#!/usr/bin/python3
"""Log Parsing function"""

import sys


def print_metrics(code, size):
    """Print Metrics of Total file size & Status Code count."""
    print("File size: {:d}".format(size))
    for i in sorted(code.keys()):
        if code[i] != 0:
            print("{}: {:d}".format(i, code[i]))


status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}

size = 0
count = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_metrics(status_codes, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in status_codes:
                status_codes[stlist[-2]] += 1
        except:
            pass
    print_metrics(status_codes, size)


except KeyboardInterrupt:
    print_metrics(status_codes, size)
    raise
