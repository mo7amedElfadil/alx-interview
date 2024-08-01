#!/usr/bin/python3
"""
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
        Return: fewest number of coins needed to meet total
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
