# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0,-1), (1, 0), (-1, 0)]

        n = len(grid)
        m = len(grid[0])

        def inbound(r, c):
            row_check = 0 <= r < n
            col_check = 0 <= c < m

            return row_check and col_check
        
        distance = [[float('inf') for _ in range(m)] for _ in range(n)]
    
        distance[0][0] = 0

        #spfa
        queue = deque()
        queue.append((0, 0))
        in_queue = set()
        in_queue.add((0, 0))

        while queue:
            row, col = queue.popleft()
            in_queue.discard((row, col))

            for x, y in directions:
                new_row = row + x
                new_col = col + y

                if inbound(new_row, new_col):
                    new_val = distance[row][col] + grid[row][col]
                    if new_val < distance[new_row][new_col]:
                        distance[new_row][new_col] = new_val
                        if (new_row, new_col) not in in_queue:
                            in_queue.add((new_row, new_col))
                            queue.append((new_row, new_col)) 

        
        return distance[n-1][m-1]
        