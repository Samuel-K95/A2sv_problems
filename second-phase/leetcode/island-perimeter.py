class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        count = 0
        visited = set()

        def dfs(grid, visited, row, col):
            nonlocal count
            visited.add((row, col))

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and  (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    dfs(grid, visited, new_row, new_col)
                elif not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    count += 1
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(grid, visited, i,  j)
                

        return count