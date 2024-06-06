"""
You have a set of integers s, which originally contains all the numbers
from 1 to n. Unfortunately, due to some error, one of the numbers in s got
duplicated to another number in the set, which results in repetition of one
number and loss of another number.
You are given an integer array nums representing the data status of this set
after the error.
Find the number that occurs twice and the number that is missing and return
them in the form of an array.

Input: nums = [1,2,2,4]
Output: [2,3]

Input: nums = [1,1]
Output: [1,2]
"""


# Hashmap solution, Space: O(n) Time: O(n)
# def findErrorNums(nums: list[int]) -> list[int]:
#     arr = []
#     seen = set()
#     for num in nums:
#         if num not in seen:
#             seen.add(num)
#         else:
#             arr.append(num)
#
#     for i in range(1, len(nums) + 1):
#         if i not in seen:
#             arr.append(i)
#             break
#
#     return arr

# Inplace Solution, Time: O(n) Space: O(1)
def findErrorNums(nums: list[int]) -> list[int]:
    res = [0, 0]  # [Duplicate, Missing]

    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            res[0] = n
        nums[n - 1] = -nums[n - 1]

    for i, n in enumerate(nums):
        if n > 0 and (i + 1) != res[0]:
            res[1] = i + 1
    return res


print(findErrorNums([3, 2, 3, 4, 6, 5]))

# print(findErrorNums([1, 2, 2, 4]))
# print(findErrorNums([1, 1]))
