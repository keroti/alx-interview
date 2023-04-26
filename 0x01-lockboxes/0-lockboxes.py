#!/usr/bin/python3
""" Script to determine if all boxes can be opened """


def canUnlockAll(boxes):
    """
        This function will take a list of lists
        and the content of a list will unlock other lists
    """
    n = len(boxes)
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < n:
                keys.append(box)
    if len(keys) == n:
        return True
    return False
