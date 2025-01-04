"""
Two Sum

"""

def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}

    for i in range(len(nums)):
        if (target - nums[i]) in map:
            return [i, map[target - nums[i]]]
        map[nums[i]] = i
