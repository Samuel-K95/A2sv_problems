# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left <= right:
            middle = left + (right - left) // 2
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] < middle:
                        cnt += 1

            if cnt < k:
                left = middle + 1
            else:
                right = middle - 1
    
        return right