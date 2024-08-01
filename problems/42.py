"""
Trapping Rain Water

Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.
"""

# Time: O(n) Space: O(n)
# def trap(height: list[int]) -> int:
#     res = 0

#     maxLeft, maxRight = [0] * len(height), [0] * len(height)

#     maxLeftTillNow = 0
#     for i in range(len(height)):
#         maxLeft[i] = maxLeftTillNow
#         maxLeftTillNow = max(maxLeftTillNow, height[i])

#     maxRightTillNow = 0
#     for i in range(len(height) - 1, -1, -1):
#         maxRight[i] = maxRightTillNow
#         maxRightTillNow = max(maxRightTillNow, height[i])

#     for i in range(len(height)):
#         res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)

#     return res

# Time: O(n) Space: O(1)
# 2 pointer approach: We always shift the minimum of two pointers
def trap(height: list[int]) -> int:
    if not height: return 0

    l, r = 0, len(height) - 1
    maxLeftTillNow, maxRightTillNow = height[l], height[r]
    res = 0

    while l < r:
        if maxLeftTillNow <= maxRightTillNow:
            l += 1
            maxLeftTillNow = max(maxLeftTillNow, height[l])
            res += maxLeftTillNow - height[l]
        else:
            r -= 1
            maxRightTillNow = max(maxRightTillNow, height[r])
            res += maxRightTillNow - height[r]

    return res
