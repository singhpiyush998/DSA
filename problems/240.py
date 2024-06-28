"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    i = 0
    j = len(matrix[i]) - 1

    while i < len(matrix) and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return True

    return False


print(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
      3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
