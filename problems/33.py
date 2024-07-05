"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] >= nums[0]:
            if target > nums[m] or target < nums[0]:
                l = m + 1
            else:
                if target < nums[0]:
                    l = m + 1
                else:
                    r = m - 1
        else:
            if target < nums[m]:
                r = m - 1
            else:
                if target <= nums[-1]:
                    l = m + 1
                else:
                    r = m -1

    return -1

print(search([5,1,3], 5))
print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))
