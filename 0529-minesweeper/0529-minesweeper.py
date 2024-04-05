class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
        nums = {'1', '2', '3', '4', '5', '6', '7', '8'}

        def inbound(i, j):
            row_check = 0 <= i < len(board)
            col_check = 0 <= j < len(board[0])
            return row_check and col_check

        def check_for_mine(i, j):
            mines = 0
            for x, y in directions:
                newx = i + x
                newy = j + y
                if inbound(newx, newy) and board[newx][newy] == 'M':
                    mines += 1
            return mines
        
        def dfs(row, col):
            if board[row][col] in nums:
                return
            
            if board[row][col] != 'M':
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y
                    mines = check_for_mine(row, col)
                    if mines == 0:
                        board[row][col] = 'B'
                    else:
                        board[row][col] = str(mines)
                        return

                    if inbound(new_row, new_col) and board[new_row][new_col] != 'B':
                        dfs(new_row, new_col)
            else:
                return

        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])
        
        return board
