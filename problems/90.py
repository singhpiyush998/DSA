"""
Subsets 2

Given an integer array nums that may contain
duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order
"""


def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    res = []

    nums.sort()
    def backtrack(currSubset: list[int], index: int):
        # The Goal
        if index == len(nums):
            res.append(currSubset.copy())
            return

        # The Choices
        # Include the number
        currSubset.append(nums[index])
        backtrack(currSubset, index + 1)
        currSubset.pop()

        # Ignore the number (and all its duplicates)
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        backtrack(currSubset, index + 1)

    backtrack([], 0)
    return res
