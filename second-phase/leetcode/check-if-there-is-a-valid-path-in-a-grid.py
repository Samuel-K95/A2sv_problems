class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        path = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(0, 1), (-1, 0)]
        }

        def inbound(i, j):
            row_check = 0 <= i < len(grid)
            col_check = 0 <= j < len(grid[0])

            return row_check and col_check

        def check_front(i, j, new_i , new_j):
            next = grid[new_i][new_j]
            curr = grid[i][j]
            if curr == 1:
                if next == 3 or next == 5 or next == 1:
                    return True
            elif curr == 2:
                if next == 5 or next == 6 or next == 2:
                    return True
            elif curr == 3:
                if next == 5 or next == 6 or next == 2:
                    return True
            elif curr == 4:
                if next == 1 or next == 3 or next == 5:
                    return True
            elif curr == 5:
                if next == 3 or next == 4 or next == 2:
                    return True
            elif curr == 6:
                if next == 1 or next == 3 or next == 5:
                    return True

            return False
        def check_back(i, j, new_i, new_j):
            next = grid[new_i][new_j]
            curr = grid[i][j]
            if curr == 1:
                if next == 4 or next == 6 or next == 1:
                    return True
            elif curr == 2:
                if next == 3 or next == 4 or next == 2:
                    return True
            elif curr == 3:
                if next == 4 or next == 6 or next == 1:
                    return True
            elif curr == 4:
                if next == 2 or next == 5 or next == 6:
                    return True
            elif curr == 5:
                if next == 1 or next == 4 or next == 6:
                    return True
            elif curr == 6:
                if next == 2 or next == 3 or next == 4:
                    return True

            return False
        
        visited = set()

        def dfs(i, j):
            if i == len(grid)-1 and j == len(grid[0]) - 1:
                return True
            visited.add((i, j))
            way = path[grid[i][j]]
            for k in range(len(way)):
                new_row = i + way[k][0]
                new_col = j + way[k][1]

                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    if k == 0:
                        if check_front(i, j, new_row, new_col):
                            found = dfs(new_row, new_col)

                            if found:
                                return True

                    if k == 1:
                        if check_back(i, j, new_row, new_col):
                            found = dfs(new_row, new_col)

                            if found:
                                return True
            return False
        
        return dfs(0, 0)
        
                    


