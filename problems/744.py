"""
You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.
"""


def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1
    target = ord(target)

    res = letters[0]

    while l <= r:
        m = (l + r) // 2
        mid = ord(letters[m])

        if mid > target:
            res = letters[m]
            r = m - 1
        else:
            l = m + 1

    return res
