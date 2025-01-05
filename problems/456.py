"""
132 Pattern

Given an array of n integers nums,
a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

# Monotonic Decreasing stack
# because for each k value we want to find a j value which is larger than it
def find132pattern(nums: list[int]) -> bool:
    stack = [] # pair - [num, minValLeft]
    currMin = nums[0]

    for n in nums[1:]: # skip 1st because it can't be j or k value only i which is already in currMin
        while stack and stack[-1][0] <= n:
            stack.pop()

        if stack and stack[-1][1] < n:
            return True
        stack.append((n, currMin))
        currMin = min(currMin, n)

    return False
