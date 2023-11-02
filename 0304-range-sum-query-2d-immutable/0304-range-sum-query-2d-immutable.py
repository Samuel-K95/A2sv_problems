class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # build ps 2D ps Table (PS)
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.ps[r][c] = (
                    self.ps[r][c - 1]
                    + self.ps[r - 1][c]
                    - self.ps[r - 1][c - 1]
                    + matrix[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.ps[row2 + 1][col2 + 1]
            - self.ps[row1][col2 + 1]
            - self.ps[row2 + 1][col1]
            + self.ps[row1][col1]
        )