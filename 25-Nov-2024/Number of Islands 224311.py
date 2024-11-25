# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def inbound(r, c):
            row_check = 0 <= r < n
            col_check = 0 <= c < m

            return row_check and col_check
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0

        def bfs(r, c):
            grid[r][c] = "0"
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y

                    if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                        grid[new_row][new_col] = "0"
                        queue.append((new_row, new_col))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs(i, j)
        
        return cnt




