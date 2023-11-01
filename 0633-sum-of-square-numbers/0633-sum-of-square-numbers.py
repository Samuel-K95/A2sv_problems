class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            ans = (left**2) + (right**2)
            if ans > c:
                right -= 1
            elif ans < c:
                left += 1
            else:
                return True
        return False