class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        targ_row = []

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                targ_row = matrix[mid]

            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(targ_row) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if targ_row[mid] == target:
                return True
            
            if targ_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
            