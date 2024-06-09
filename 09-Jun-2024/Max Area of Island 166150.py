# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])

        def inbound(r, c):
            row_check = 0 <= r < n
            col_check =  0 <= c < m

            return row_check and col_check
        

        def dfs(i, j):

            curr = 1
            for r, c in directions:
                new_row = i + r
                new_col = j + c

                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 0
                    curr += dfs(new_row, new_col)
            
            return curr
        

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(ans, dfs(i, j))
        
        return ans

