# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat) + 1
        m = len(mat[0])  + 1

        def row_check(r):
            return 1 <= r < n
        
        def col_check(c):
            return 1 <= c < m
        

        pref = [[0 for _ in range(m)] for i in range(n)]
        

        for r in range(1, n):
            for c in range(1, m):
                pref[r][c] = pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1] + mat[r-1][c-1]
            
        ans = []
        for r in range(1, n):
            curr = []
            for c in range(1, m):
                r1 = r - k if row_check(r-k) else 1
                r2 = r + k if row_check(r + k) else n - 1

                c1 = c - k if col_check(c-k) else 1
                c2 = c + k if col_check(c + k) else m - 1

                curr_ans = pref[r2][c2] - pref[r2][c1-1] - pref[r1-1][c2] + pref[r1-1][c1-1]

                curr.append(curr_ans)

            ans.append(curr)

        return ans



