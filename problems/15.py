"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    
    for i, x in enumerate(nums):
        if i > 0 and x == nums[i - 1]:
            continue
        
        # Two sum 2: Use a left and right pointer
        l, r = i + 1, len(nums) - 1
        while l < r:
            y, z = nums[l], nums[r]
            threeSum = x + y + z
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([x, y, z])
                r -= 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
    return res

print(threeSum([-3, 3, 4, -3, 1, 2]))
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0, 0, 0, 0]))
