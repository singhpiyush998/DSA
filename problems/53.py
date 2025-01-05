"""
Maximum Subarray

Given an integer array nums, find the subarray
with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""


# Anytime we find a negative prefix, we increment the left pointer
# The negative prefix does not have to be one element but it can be
# composed of many elements, so we will have to consider the current sum
# as the prefix and if it is negative and curr element is positive then
# we increment left pointer to the current element
# the right pointer is the one going from start to end.
# Basically, until my current subarray's sum becomes -ve, we keep it going
def maxSubArray(nums: list[int]) -> int:
    maxSum = nums[0]
    currSum = 0
    for num in nums:
        currSum += num
        maxSum = max(maxSum, currSum)

        if currSum < 0:
            currSum = 0

    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
