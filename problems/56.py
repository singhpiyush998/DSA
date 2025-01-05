"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that
cover all the intervals in the input.
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key = lambda i: i[0]) # sort by the start value of each ihnterval
    res = [intervals[0]]

    for start, end in intervals[1:]:
        prevEnd = res[-1][1]
        # overlap: start of current interval <= end of previous interval
        if start <= prevEnd:
            res[-1][1] = max(end, prevEnd)
        else:
            res.append([start, end])

    return res
