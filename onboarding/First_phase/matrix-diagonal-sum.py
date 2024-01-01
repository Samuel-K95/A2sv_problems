class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summat = 0
        for row in range(len(mat)):
            for col in range(len(mat)):
                if row == col:
                    summat += mat[row][col]
                    summat += mat[row][len(mat) - col - 1]
        return summat if len(mat) % 2 == 0 else summat - mat[len(mat)//2][len(mat)//2]
