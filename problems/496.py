"""
Next Greater Element I

The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where
nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2. If there is no
next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater
element as described above.
"""

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    res = [-1] * len(nums1)

    nums1ValToIndex = {n:i for i, n in enumerate(nums1)}
    stack = []

    for n in nums2:
        while stack and stack[-1] < n:
            val = stack.pop()
            res[nums1ValToIndex[val]] = n

        if n in nums1ValToIndex:
            stack.append(n)

    return res
