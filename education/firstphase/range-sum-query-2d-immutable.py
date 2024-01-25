class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.pref = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[0]) + 1):
                self.pref[r][c] = matrix[r-1][c-1] + self.pref[r-1][c] + self.pref[r][c-1] - self.pref[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.pref[row2+1][col2+1] - self.pref[row1][col2 + 1] - self.pref[row2 + 1][col1] + self.pref[row1][col1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)