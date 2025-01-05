"""
Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}

    for i in range(len(nums)):
        if (target - nums[i]) in map:
            return [i, map[target - nums[i]]]
        map[nums[i]] = i
