#!/usr/bin/python3
"""
Making Change function"""


def makeChange(coins, total):
    """This function will determine the fewest
    number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for j in coin:
            while (total >= j):
                counter += 1
                total -= j
        if total == 0:
            return counter
        return -1
