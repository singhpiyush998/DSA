"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


# TIME: O(m + n)
# def searchMatrix(matrix: list[list[int]], target: int) -> bool:
#     for row in matrix:
#         if row[-1] >= target:
#             return target in row
#     return False


# TIME: O(log(m * n))
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    nRow, nCol = len(matrix), len(matrix[0])
    l, r = 0, nRow * nCol - 1

    while l <= r:
        mid = (l + r) // 2
        if matrix[mid // nCol][mid % nCol] < target:
            l = mid + 1
        elif matrix[mid // nCol][mid % nCol] > target:
            r = mid - 1
        else:
            return True
    return False
