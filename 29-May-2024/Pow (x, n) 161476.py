# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            store = self.myPow(1/x, n // 2)
            if n % 2 == 0:
                return store ** 2
            else:
                return (store ** 2) * (1 / x)
        else:
            store = self.myPow(x, n //2)
            if n % 2 == 0:
                return store ** 2
            else:
                return (store ** 2) * x
