"""
Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color
red, white, and blue, respectively.

You must solve this problem without using the library's sort function
"""

def sortColors(self, nums: list[int]) -> None:
    i, l, r = 0, 0, len(nums) - 1

    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            i, l = i + 1, l + 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1
