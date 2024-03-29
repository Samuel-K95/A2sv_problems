class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        def factorize(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n%d == 0:
                    n /= d
                    factors.add(d)
                d += 1
            if n > 1:
                factors.add(n)

            return factors
        
        fact = factorize(n)
        for i in fact:
            if i != 2 and i != 3 and i != 5:
                return False

        return True
        
