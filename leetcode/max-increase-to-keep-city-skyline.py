class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                col[j].append(grid[i][j])
        fin = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                rowMax = max(grid[i])
                colMax = max(col[j])
                fin += (min(rowMax, colMax)) - grid[i][j]
        return fin
