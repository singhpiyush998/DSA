"""
Find the Duplicate Number

Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums
and use only constant extra space.
"""

# Algorithm: Floyd's to find the beginning of the cycle
# Time: O(n) Space: O(1)
def findDuplicate(nums: list[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow: break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2: break

    return slow
