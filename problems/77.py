"""
Combinations

Given two integers n and k,
return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.
"""

# Time: O(k * n^k) Space: O(k)
def combine(n: int, k: int) -> list[list[int]]:
    res = []

    def backtrack(combination: list[int], lastChosenDigit: int):
        # Goal
        if len(combination) == k:
            res.append(combination.copy())
            return

        # Choices
        for num in range(lastChosenDigit + 1, n + 1):
            combination.append(num)
            backtrack(combination, num)
            combination.pop()

    backtrack([], 0)
    return res
