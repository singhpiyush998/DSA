"""
Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted
"""

def findMaxAverage(self, nums: List[int], k: int) -> float:
    l = 0
    max_avg = -100000
    curr_sum = 0

    for r in range(len(nums)):
        curr_sum += nums[r]

        if (r - l + 1) == k:
            curr_avg = curr_sum / k
            max_avg = max(max_avg, curr_avg)
            curr_sum -= nums[l]
            l += 1

    return max_avg