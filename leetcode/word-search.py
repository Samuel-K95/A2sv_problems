class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def inbound(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            return True

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if not inbound(i, j) or (i, j) in vis:
                return False

            if board[i][j] != word[k]:
                return False

            vis.add((i, j))


            for x, y in DIR:
                if dfs(i+x, j+y, k+1):
                    return True

            vis.remove((i, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False





