"""
Permutations II

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []

    # To make unique choices per level
    count = Counter(nums)

    def backtrack(currPerm: list[int]):
        # Our Goal
        if len(currPerm) == len(nums):
            res.append(currPerm.copy())
            return

        # Our Choices
        for num in count:
            # To make sure we don't choose the same number multiple times
            if count[num] > 0:
                currPerm.append(num)
                count[num] -= 1
                backtrack(currPerm)
                currPerm.pop()
                count[num] += 1

    backtrack([])
    return res
