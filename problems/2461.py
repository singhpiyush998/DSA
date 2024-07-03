"""
MAXIMUM SUM OF DISTINCT SUBARRAYS WITH LENGTH K

You are given an integer array nums and an integer k. Find the maximum subarray 
sum of all the subarrays of nums that meet the following conditions:
    The length of the subarray is k, and
    All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions.
If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import Counter

def maximumSubarraySum(nums: list[int], k: int) -> int:
    freq = Counter(nums[:k])

    res = 0
    total = sum(nums[:k])
    if len(freq) == k:
        res = total
    for i in range(k, len(nums)):
        freq[nums[i]] += 1
        freq[nums[i - k]] -= 1
        if freq[nums[i - k]] == 0:
            del freq[nums[i - k]]

        total += nums[i]
        total -= nums[i - k]
        if len(freq) == k:
            res = max(res, total)
        
    return res

print(maximumSubarraySum([1,1,1,7,8,9], 3))
print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
