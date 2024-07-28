"""
Permutations

Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.
"""

# Time: O(n! * n) Space: O(n! * n)
def permute(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(permutation: list[int], chosenNums: set[int]):
        # Our Goal
        if len(permutation) == len(nums):
            res.append(permutation.copy())
            return

        # Our Choices
        for num in nums:
            if num not in chosenNums: # leftNums
                permutation.append(num)
                chosenNums.add(num)
                backtrack(permutation, chosenNums)
                chosenNums.remove(num)
                permutation.pop()
    backtrack([], set())
    return res

# Time: O(n! * n^2) Space: O(n! * n)
# def permute(nums: list[int]) -> list[list[int]]:
#     res = []

#     def backtrack(chosenNums: list[int], leftNums: list[int]):
#         # Our Goal
#         if len(chosenNums) == len(nums):
#             res.append(chosenNums.copy())
#             return

#         # Our choices
#         for num in leftNums:
#             chosenNums.append(num)
#             leftNums = list(filter(lambda x: x not in chosenNums, nums))
#             backtrack(chosenNums, leftNums)
#             chosenNums.pop()

#     backtrack([], nums)
#     return res
