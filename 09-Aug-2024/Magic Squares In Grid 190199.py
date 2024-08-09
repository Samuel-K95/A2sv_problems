# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inbound(r, c):
            row_check = 0 <= r < n
            col_check = 0 <= c < m
            return row_check and col_check

        cnt = 0

        for r in range(n):
            for c in range(m):
                dist = defaultdict(set)
                if inbound(r-1, c-1) and inbound(r+1, c-1):
                    if inbound(r-1, c+1) and inbound(r+1, c+1):
                        row_one = grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1]
                        if grid[r-1][c-1] not in dist['row'] and grid[r-1][c-1] < 10 and grid[r-1][c-1] > 0:
                            dist['row'].add(grid[r-1][c-1])
                        if grid[r-1][c] not in dist['row'] and grid[r-1][c] < 10 and grid[r-1][c] > 0:
                            dist['row'].add(grid[r-1][c])
                        if grid[r-1][c+1] not in  dist['row'] and grid[r-1][c+1] <10 and grid[r-1][c+1] > 0:
                            dist['row'].add(grid[r-1][c+1])

                        row_two = grid[r][c-1] + grid[r][c] + grid[r][c+1]
                        if grid[r][c-1] not in dist['row'] and grid[r][c-1] < 10 and grid[r][c-1] > 0:
                            dist['row'].add(grid[r][c-1])
                        if grid[r][c] not in dist['row'] and grid[r][c] < 10 and grid[r][c] > 0:
                            dist['row'].add(grid[r][c])
                        if grid[r][c+1] not in dist['row'] and grid[r][c+1] <10 and grid[r][c+1]  > 0:
                            dist['row'].add(grid[r][c+1])


                        row_three = grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1]
                        if grid[r+1][c-1] not in dist['row'] and grid[r+1][c-1] < 10 and grid[r+1][c-1] > 0:
                            dist['row'].add(grid[r+1][c-1])
                        if grid[r+1][c] not in dist['row'] and grid[r+1][c] < 10 and grid[r+1][c]  > 0:
                            dist['row'].add(grid[r+1][c])
                        if grid[r+1][c+1] not in dist['row'] and grid[r+1][c+1] <10 and grid[r+1][c + 1]  > 0:
                            dist['row'].add(grid[r+1][c+1])
                        
                        rows = row_one == row_two == row_three and len(dist['row']) == 9

                        col_one = grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1]
                        col_two = grid[r-1][c] + grid[r][c] + grid[r+1][c]
                        col_three = grid[r-1][c+1] + grid[r][c+1] + grid[r+1][c+1]
                        cols = col_one == col_two == col_three and len(dist['row']) == 9

                        diag_one = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
                        diag_two = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
                        diags = diag_one == diag_two and len(dist['row']) == 9

                        if rows == True and cols == True and diags == True :
                            cnt += 1
                        # dist['row'].clear()
        return cnt