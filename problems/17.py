"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.
"""

# Time: O(n . 4^n)
def letterCombinations(digits: str) -> list[str]:
    res = []
    digitToChar = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }

    def backtrack(i, currStr):
        if len(currStr) == len(digits):
            res.append(currStr)
            return

        for c in digitToChar[digits[i]]:
            backtrack(i + 1, currStr + c)

    if digits:
        backtrack(0, "")

    return res
