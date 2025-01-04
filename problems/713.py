"""
Subarray Product Less Than K

Given an array of integers nums and an integer k,
return the number of contiguous subarrays
where the product of all the elements
in the subarray is strictly less than k.
"""

def numSubarrayProductlessThanK(self, nums: list[int], k: int) -> int:
    res = 0

    l = 0
    currProduct = 1
    for r in range(len(nums)):
        currProduct *= nums[r]

        while currProduct >= k and l <= r:
            currProduct = currProduct // nums[l]
            l += 1

        res += (r - l + 1)


    return res
