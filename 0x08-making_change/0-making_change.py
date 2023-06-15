#!/usr/bin/python3
"""
Make Change module
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values
    Return: fewest number of coins needed to meet total
    """
    if total < 0:
        return 0
    if total == 0:
        return 0
    if coins == []:
        return -1

    few_coins = [float('inf')] * (total + 1)
    few_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i and few_coins[i - coin] + 1 < few_coins[i]:
                few_coins[i] = few_coins[i - coin] + 1

    return few_coins[total] if few_coins[total] != float('inf') else -1
