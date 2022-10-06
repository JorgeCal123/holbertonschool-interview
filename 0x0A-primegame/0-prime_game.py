#!/usr/bin/python3
""" project prime game"""


def isWinner(x, nums):
    for i in nums:
        for j in range(1,nums[i]):
            print(j)