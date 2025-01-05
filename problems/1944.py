"""
Number of Visible People in a Queue

There are n people standing in a queue, and they numbered from 0 to n - 1 in
left to right order. You are given an array heights of distinct integers where
heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in
between is shorter than both of them.

Return an array answer of length n where answer[i] is the number of people the
ith person can see to their right in the queue
"""

def canSeePersonsCount(heights: list[int]) -> list[int]:
    res = [0] * len(heights)

    stack = [] # height
    for i in range(len(heights) - 1, -1, -1):
        while stack and stack[-1] < heights[i]:
            stack.pop()
            res[i] += 1

        if stack:
            res[i] += 1

        stack.append(heights[i])

    return res
