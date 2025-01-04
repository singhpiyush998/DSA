"""
Merge Sorted Arrays

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

"""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    l, r = m - 1, n - 1

    i = m + n - 1
    while l >= 0 and r >= 0:
        if nums1[l] > nums2[r]:
            nums1[i] = nums1[l]
            l -= 1
        else:
            nums1[i] = nums2[r]
            r -= 1
        i -= 1

    while r >= 0:
        nums1[i] = nums2[r]
        i, r = i - 1, r - 1
