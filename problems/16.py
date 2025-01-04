"""
3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution
"""

def threeSumClosest(self, nums: list[int], target: int) -> int:
    res = 0
    nums.sort()

    lowestDistanceFromTarget = 100001
    for i, x in enumerate(nums):
       l, r = i + 1, len(nums) - 1
       while l < r:
           y, z = nums[l], nums[r]
           threeSum = x + y + z

           distanceFromTarget = abs(target - threeSum)
           if distanceFromTarget < lowestDistanceFromTarget:
               res = threeSum
               lowestDistanceFromTarget = distanceFromTarget

           if threeSum < target:
               l += 1
           elif threeSum > target:
               r -= 1
           else:
               return threeSum

    return res
