class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        dup = [[0] * row for i in range(col)]
        for i in  range(col):
            for j in range(row):
                dup[i][j] = matrix[j][i]
        return dup