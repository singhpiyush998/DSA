"""
Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order
"""

def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []

    def backtrack(currComb: list[int], lastAddedDigit: int, currSum: int):
        # The goal
        if len(currComb) == k:
            if currSum == n:
                res.append(currComb.copy())
            return

        # The constraint
        if currSum >= n:
            return

        # The choices
        for number in range(lastAddedDigit + 1, 9 + 1):
            currComb.append(number)
            currSum += number

            backtrack(currComb, number, currSum)

            currComb.pop()
            currSum -= number

    backtrack([], 0, 0)
    return res
