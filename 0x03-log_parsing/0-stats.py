#!/usr/bin/python3
import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        code = parts[-2]
        size = int(parts[-1])
        if code in status_codes:
            status_count[code] += 1
        total_size += size
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print("{}: {}".format(code, status_count[code]))
    except Exception:
        pass

print("File size: {}".format(total_size))
for code in sorted(status_count.keys()):
    if status_count[code] > 0:
        print("{}: {}".format(code, status_count[code]))
