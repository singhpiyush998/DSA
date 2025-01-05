"""
Maximum Subarray Minimum Product
"""


"""
stack[start, value]
start - subarray start index
value - minimum value in the subarray

Consider if each value was the min of subarray

if the stack is not empty after the complete iteration of input array, then
the end index of a given value's subarray is the end of the input array
"""


def maxSumMinProduct(nums: list[int]) -> int:
    res = 0
    stack = [] # monotonic increasing stack
    prefixSum = [0]
    for n in nums:
        prefixSum.append(prefixSum[-1] + n)

    for i, n in enumerate(nums):
        newStart = i
        while stack and stack[-1][1] > n:
            start, val = stack.pop()
            totalSum = prefixSum[i] - prefixSum[start] # end - start
            res = max(res, val * totalSum)
            newStart = start

        stack.append((newStart, n))

    # if the stack is not empty after iteration
    for start, val in stack:
        totalSum = prefixSum[-1] - prefixSum[start]
        res = max(res, val * totalSum)

    return res % (10 ** 9 + 7)
