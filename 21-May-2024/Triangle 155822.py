# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top down
        # mem = {}

        # def dp(i, j):
        #     if i >= len(triangle) or j >= len(triangle[i]):
        #         return 0
            
        #     if (i, j) not in mem:
        #         mem[(i, j)] = triangle[i][j] + min(dp(i+1, j+1), dp(i+1, j))
            
        #     return mem[(i, j)]
        

        # return dp(0, 0)

        # bottom up

        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
        
        return triangle[0][0]


