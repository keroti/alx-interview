#!/usr/bin/python3
'''Module for log parsing'''


import sys

status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
size = 0
counter = 0

try:
    for i in sys.stdin:
        list = i.split(" ")
        if len(list) > 4:
            code = list[-2]
            size = int(list[-1])
            if code in status_code.keys():
                status_code[code] += 1
            size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
