"""
Subsets

Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""

# Time: O(2^n * n) Space: O(n * 2^n)
def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def backtrack(subset: list[int], lastChosenDigitIndex: int):
        # Goal
        res.append(subset.copy())

        # Choices
        for index in range(lastChosenDigitIndex + 1, len(nums)):
            subset.append(nums[index])
            backtrack(subset, index)
            subset.pop()

    backtrack([], -1)
    return res
