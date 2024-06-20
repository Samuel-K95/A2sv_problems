# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        def inbound(i, j):
            row_check = 0 <= i < n + 1
            col_check = 0 <= j < m + 1
            return row_check and col_check
        
        pos = [(-1, 0), (0, -1), (-1, -1)]
        for row in range(1, n+1):
            for col in range(1, m+1):
                small = float('inf')
                if matrix[row-1][col-1] == "1":
                    for r, c in pos:
                        new_row, new_col = row + r, col + c
                        if inbound(new_row, new_col):
                            small = min(small, dp[new_row][new_col])
                    small += 1
                else:
                    small = 0
                    
                dp[row][col] = small
        
        mx = 0
        for i in range(n + 1):
            for j in range(m + 1):
                mx = max(mx, dp[i][j])
        return mx * mx
                



