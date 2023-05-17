#!/usr/bin/python3
"""
UTF-8 Validation module
"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        if num_bytes == 0:

            while mask1 & byte:
                num_bytes += 1
                mask1 >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if byte & mask1 or not byte & mask2:
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
