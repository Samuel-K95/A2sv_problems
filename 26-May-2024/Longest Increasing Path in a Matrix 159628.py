# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])

        def inbound(i, j):
            row_check = 0 <= i < m
            col_check = 0  <= j < n

            return row_check and col_check
        
        vis = set()

        mem = {}
        def dfs(i, j):
            curr = 0
            if (i, j) not in mem:
                for r, c in directions:
                    new_row = i + r
                    new_col = j + c

                    if inbound(new_row, new_col) and matrix[new_row][new_col] > matrix[i][j] and (new_row, new_col) not in vis:
                        curr = max(curr, dfs(new_row, new_col))
                mem[(i, j)] = curr+1
            
            return mem[(i, j)]
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        
        return ans
        

        
            




        
