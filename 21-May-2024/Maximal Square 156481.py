# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        grid = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1':
                    if row == 0 or col == 0:
                        grid[row][col] = 1
                    else:
                        minimum = min(grid[row][col-1], grid[row-1][col], grid[row-1][col-1])
                        grid[row][col] = minimum + 1
                    ans = max(ans, grid[row][col])
        
        return ans ** 2