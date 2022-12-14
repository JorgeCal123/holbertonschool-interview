#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    total_coins = 0
    sum_coins = 0
    for coin in coins:
        while sum_coins <= total:
            sum_coins += coin
            total_coins += 1
            if sum_coins == total:
                break
            if sum_coins > total:
                total_coins -= 1
                sum_coins -= coin
                break
    if sum_coins != total:
        return -1
    return total_coins
