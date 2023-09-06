#!/usr/bin/python3
"""
Module for prime game
"""


def primeNumbers(n):
    """
    Function to return a list of prime numbers
    """
    primeNums = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNums.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNums


def isWinner(x, nums):
    """
    Function to determine who the winner of the game is
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNums = primeNumbers(nums[i])
        if len(primeNums) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
