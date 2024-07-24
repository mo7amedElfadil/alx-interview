#!/usr/bin/env python3
"""
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
        Return: fewest number of coins needed to meet total
        81 = 25 + 25 + 25 + 5 + 1

    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    count = 0
    for coin in coins:
        while total >= coin:
            div = total // coin
            count += div
            total -= coin * div
    if total != 0:
        return -1
    return count
