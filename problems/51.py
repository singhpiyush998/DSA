"""
N-Queens

The n-queens puzzle is the problem of placing n queens
on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        self.nQueens(n, 0, [], res)
        return res

    def nQueens(self, n: int, row: int, colPlacements: list[int], res: list[list[str]]):
        if row == n:
            res.append(self.getStringRepresentation(n, colPlacements))
        else:
            for col in range(n):
                colPlacements.append(col)
                if self.isValid(colPlacements):
                    self.nQueens(n, row + 1, colPlacements, res)
                colPlacements.pop()

    def isValid(self, colPlacements: list[int]) -> bool:
        currRowIndex = len(colPlacements) - 1
        for i in range(currRowIndex):
            diff = abs(colPlacements[i] - colPlacements[currRowIndex])
            if diff == 0 or diff == (currRowIndex - i):
                return False
        return True

    def getStringRepresentation(self, n:int, colPlacements: list[int]) -> list[str]:
        res = []
        for col in colPlacements:
            strRep = "." * col + "Q" + "." * ((n - 1) - col)
            res.append(strRep)
        return res
