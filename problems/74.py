def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if row[-1] >= target:
            return target in row
    return False
