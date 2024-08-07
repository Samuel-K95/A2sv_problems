# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        collect = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    collect.append([r, c])
        
        def inbound(r, c):
            row_check = 0 <= r < len(matrix)
            col_check = 0 <= c < len(matrix[0])

            return row_check and col_check

        for r, c in collect:
            x, y = r, c
            while inbound(x, c):
                matrix[x][c] = 0
                x += 1
            x = r
            while inbound(x, c):
                matrix[x][c] = 0
                x -= 1
            while inbound(r, y):
                matrix[r][y] = 0
                y += 1
            y = c
            while inbound(r, y):
                matrix[r][y] = 0
                y -= 1
        


