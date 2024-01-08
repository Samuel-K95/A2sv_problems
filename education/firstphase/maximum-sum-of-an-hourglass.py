class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j - 1 >= 0 and j + 1 < len(grid[i]) and i + 2 < len(grid):
                    hourglass = grid[i][j-1] + grid[i][j] + grid[i][j + 1] + grid[i+1][j]
                    hourglass += grid[i + 2][j-1] + grid[i + 2][j] + grid[i + 2][j + 1]
                    ans = max(ans, hourglass)
        return ans