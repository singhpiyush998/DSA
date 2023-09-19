"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    for i, x in enumerate(nums):
        visited = set()
        for y in nums[i + 1:]:
            # two sum: if target - value not in visted then add value to visited
            # x + y + z = 0
            # x = -y - z => y + z = -x
            # therefore target is -x and value is y
            if (z := (-x - y)) in visited:
                res.append([x, y, z])
            else:
                visited.add(y)
    return res

print(threeSum([-1,0,1,2,-1,-4]))
