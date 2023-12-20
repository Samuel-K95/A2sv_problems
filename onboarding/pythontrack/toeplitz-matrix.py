class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 or j == 0:
                    continue
                else:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True
