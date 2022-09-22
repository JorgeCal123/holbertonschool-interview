#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    coins.sort(reverse = True)
    total_coins = 0
    sum_coins = 0
    if total <= 0:
        return 0
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