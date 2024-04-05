class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(i, j):
            row_check = 0 <= i < len(grid)
            col_check = 0 <= j < len(grid[0])

            return row_check and col_check

        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        graph = defaultdict(list)
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        count = 0
        second = 0
        while queue and fresh > 0:
            second += 1
            bound = len(queue)
            count = 0

            for i in range(bound):
                curr = queue.popleft()
                for x, y in directions:
                    new_row = curr[0] + x
                    new_col = curr[1] + y
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        count += 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            fresh -= count
            
        return second if fresh == 0 else -1


