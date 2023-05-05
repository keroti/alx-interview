#!/usr/bin/python3
""" Script for minimum operations """


def minOperations(n):
    """
    Calculates the minimum operation to result in exactly n H characters
    Args:
    n (int): The desired number of H characters
    Returns:
        int: The fewest number of operations needed
        to result in exactly n H characters
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return n
