class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()

        temp = [["."] * n for i in range(n)]
        ans = []

        def backtrack(row):
            if row == n:
                curr = ["".join(temp[i]) for i in range(n)]
                ans.append(curr)
                return
            
            for c in range(n):
                if c not in col and (row-c) not in pos_diag and (row+c) not in neg_diag:
                    col.add(c)
                    pos_diag.add(row-c)
                    neg_diag.add(row+c)
                    temp[row][c] = "Q"

                    backtrack(row+1)

                    col.remove(c)
                    pos_diag.remove(row-c)
                    neg_diag.remove(row+c)
                    temp[row][c] = "."
            return


        backtrack(0)

        return ans
