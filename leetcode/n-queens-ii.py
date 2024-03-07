class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos_diag = set()
        neg_diag = set()
        ans = 0

        def backtrack(r):
            nonlocal ans
            if r == n:
                ans += 1
                return
            

            for i in range(n):
                if (i in col) or (r + i in neg_diag) or (r - i in pos_diag):
                    continue

                col.add(i)
                neg_diag.add(r+i)
                pos_diag.add(r-i)

                backtrack(r+1)

                col.remove(i)
                neg_diag.remove(r+i)
                pos_diag.remove(r-i)

            return

        backtrack(0)

        return ans
