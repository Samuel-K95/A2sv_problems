class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        store = defaultdict(list)
        row = defaultdict(list)
        col = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    col[j].append(board[i][j])
                    row[i].append(board[i][j])
                    if i < 3 and j < 3:
                        store[0].append(board[i][j])
                    elif i < 3 and j >= 3 and j < 6:
                        store[1].append(board[i][j])
                    elif i < 3 and j >= 6:
                        store[2].append(board[i][j])
                    elif i >= 3 and i < 6 and j < 3:
                        store[3].append(board[i][j])
                    elif i >= 3  and i < 6 and  j >= 3 and j < 6:
                        store[4].append(board[i][j])
                    elif i >= 3 and i < 6 and j >= 6:
                        store[5].append(board[i][j])
                    elif i >= 6 and j < 3:
                        store[6].append(board[i][j])
                    elif i >= 6 and j >= 3 and j < 6:
                        store[7].append(board[i][j])
                    elif i >= 6 and j >= 6:
                        store[8].append(board[i][j])
        for j in range(9):
            if len(set(row[j])) != len(row[j]):
                return False
            if len(set(col[j])) != len(col[j]):
                return False
            if len(set(store[j])) != len(store[j]):
                return False
        return True

            