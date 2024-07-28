"""
Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the
chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency
of at least one of the chosen numbers is different.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i: int, curr: list[int], total: int):
        # Our Goal
        if total == target:
            res.append(curr.copy()) # We add a copy because we'll still be using the same curr list in other recursive calls
            return

        # Our Constraints
        if i >= len(candidates) or total > target:
            return

        # Our Choices
        # 1st choice
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])

        # 2nd choice
        curr.pop()
        dfs(i + 1, curr, total)


    dfs(0, [], 0)
    return res
