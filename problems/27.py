"""
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the
elements which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.
Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""


# def removeElement(nums: list[int], val: int) -> int:
#     k = 0
#     while k < len(nums):
#         if nums[k] == val:
#             i = k + 1
#             while i < len(nums) and nums[i] == val:
#                 i += 1
#             if i == len(nums):
#                 break
#             nums[k], nums[i] = nums[i], nums[k]
#         k += 1
#
#     return k

def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1

    print(nums)
    return k


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
