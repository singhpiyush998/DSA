"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
"""


# there are two sorted arrays, one to the left of inversion, one to the right
# the right sorted subarray will always have value smaller than min of left sorted array
def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= nums[0]:
            # we are in the left sorted array so look right 
            # because thats where smaller values are
            l = mid + 1
        else:
            # we are in the right sorted array
            # look left because thats where the first value is
            r = mid - 1
            res = min(res, nums[mid])
    return res
