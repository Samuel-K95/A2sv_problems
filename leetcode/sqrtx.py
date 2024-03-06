class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            curr = mid * mid
            if curr == x:
                return mid
            if curr < x:
                left = mid + 1
            elif curr > x:
                right = mid - 1
        

        return right
