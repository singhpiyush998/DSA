"""
Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order
(not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index
Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

This problem is similar to Search in Rotated Sorted Array,
but nums may contain duplicates.
Would this affect the runtime complexity? How and why?

example: 10111
"""

# Time: O(n)
def search(self, nums: list[int], target: int) -> bool:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return True

        # we know that mid is not target at this point
        # if mid is equal to left that means left is also not the target
        # so we eliminate left, by using inference property, not mid because
        # that would make it impossible to do binary search in cases where
        # it is possible
        if nums[m] == nums[l]:
            # can't determine if middle is in left or right sorted portion
            l += 1
        elif nums[m] > nums[l]:
            # middle is in left sorted portion
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            # middle is in right sorted portion
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return False
