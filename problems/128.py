"""
Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    longest = 0
    for num in nums:
        if not num - 1 in nums:
            length = 1
            while num + length in nums:
                length += 1
            longest = max(length, longest)
    return longest
