"""
You are give an array of size n. Find the maximum possible length of a
subarray such that its elements are arranged alternately either as even and odd
or odd and even
n = 5
a[] = {10, 12, 14, 7, 8}

output: 3
"""


def findMaxSubArray(a: list[int]):
    maxSubArrayLength = 0

    currSubArrayLength = 1
    for r in range(1, len(a)):
        if (a[r] + a[r-1]) % 2 == 1:
            currSubArrayLength += 1
            maxSubArrayLength = max(maxSubArrayLength, currSubArrayLength)
        else:
            currSubArrayLength = 1
    return maxSubArrayLength


print(findMaxSubArray([1, 3, 5]))
print(findMaxSubArray([2, 3, 4, 6, 10]))
print(findMaxSubArray([10, 12, 14, 7, 8]))
print(findMaxSubArray([2, 3, 4, 3, 4]))
print(findMaxSubArray([4, 5, 6]))
print(findMaxSubArray([1, 2, 3, 4, 5, 7, 9]))
