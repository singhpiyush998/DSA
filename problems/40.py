"""
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations
"""

def combinationSum2(self, candidates: list[int], target: int) -> list[List[int]]:
    res = []

    # To avoid duplicates, we want all the duplicate numbers to be
    # adjacent to each other, so it is easier to eliminate them
    candidates.sort()
    
    def backtrack(i: int, currSum: int, currComb: list[int]):
        # Our goal
        if currSum == target:
            res.append(currComb.copy())
            return
        
        # Our Constraints
        if currSum > target or i == len(candidates):
            return

        # Our Choices

        # Choice 1: Include the number
        currComb.append(candidates[i])
        backtrack(i + 1, currSum + candidates[i], currComb)
        currComb.pop()

        # Choice 2: Ignore the number(and all of its duplicates)
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        backtrack(i + 1, currSum, currComb)

    backtrack(0, 0, [])
    return res
