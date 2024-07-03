"""
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.
"""

# Time: O(n) Space: O(n)
# def rotate(nums: list[int], k: int) -> None:
#     n = len(nums)
#     res = [0] * n
#
#     for i, num in enumerate(nums):
#         res[(i + k) % n] = num
#
#     for i in range(len(nums)): 
#         nums[i] = res[i]

# Time: O(n) Space: O(1)
# approach: reverse the array, reverse the first k els, then reverse the reset of els
def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)

    def rev(l=0, r=len(nums) - 1):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r -1
    rev()    
    rev(r=k-1)
    rev(l=k)

    print(nums)

rotate([1,2,3,4,5,6,7], 3)
rotate([-1,-100,3,99], 2)
