#!/usr/bin/python3
"""
Given a text file with a single character 'H', what is the least number of
operations are requred to result in exactly n H characters in the file.
Allowed operations:
    Copy All
    Paste
"""
from math import sqrt


def minOperations(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Arguments:
        n - integer
    Returns:
        number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
