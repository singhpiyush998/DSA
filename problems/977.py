"""
Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

PS: array contains negative numbers as well
"""

def sortedSquares(nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    res = [0] * len(nums)

    i = len(nums) - 1
    while l <= r:
        if abs(nums[r]) > abs(nums[l]):
            res[i] = nums[r] * nums[r]
            r -= 1
        else:
            res[i] = nums[l] * nums[l]
            l += 1
        i -= 1

    return res
