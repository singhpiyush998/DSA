# Given an integer array nums, return an array answer 
# such that answer[i] is equal to the product of all the elements of nums except nums[i].

# from collections import deque

# def productExceptSelf(nums: list[int]) -> list[int]:
#     prefix = deque([1])
#     postfix = deque([1])
#     for i in range(len(nums) - 1):
#         prefix.append(prefix[i] * nums[i])
#     for i in range(len(nums) - 1, 0, -1):
#         postfix.appendleft(postfix[0] * nums[i])
#
#     ans = []
#     for i in range(len(nums)):
#         ans.append(prefix[i] * postfix[i])
#     return ans

# O(n)
def productExceptSelf(nums: list[int]) -> list[int]:
    ans = [1] * len(nums)
    pref = 1
    for i in range(len(nums)):
        ans[i] = pref
        pref *= nums[i]
    
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= post
        post *= nums[i]
    return ans

print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([0, 0]))
