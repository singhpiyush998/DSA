"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray
whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
"""


# def minSubArrayLen(target: int, nums: list[int]) -> int:
#     minLen = 100001
#
#     i, j = 0, 0
#     currSum = 0
#     while j < len(nums):
#         currSum += nums[j]
#         if currSum < target:
#             j += 1
#         else:
#             minLen = min(minLen, j - i + 1)
#             currSum -= nums[i]
#             currSum -= nums[j]
#             i += 1
#
#     return 0 if minLen == 100001 else minLen

def minSubArrayLen(target: int, nums: list[int]) -> int:
    l, currSum = 0, 0
    minLen = 100001
    for r in range(len(nums)):
        currSum += nums[r]
        while currSum >= target:
            minLen = min(minLen, r - l + 1)
            currSum -= nums[l]
            l += 1

    return 0 if minLen == 100001 else minLen


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
