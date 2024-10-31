"""
Peak Index in a Mountain Array

You are given an integer mountain array arr of length n
where the values increase to a peak element and then decrease.
Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity
"""

# at any index,
# we are either in the right (curr is less than its left neigbour/greater than its right neighbour),
# left (curr is greater than its left neighbour/less than its right)
# or at peak
# if right -> go left, if left -> go right
def peakIndexInMountainArray(self, arr: list[int]) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
            # at peak
            return m

        if arr[m] > arr[m - 1] or m - 1 < 0:
            # we are in left portion of peak, so move right
            l = m + 1
        elif arr[m] < arr[m - 1]:
            # we are in right portion of peak, so move left
            r = m - 1
