class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prod = 1
        for i in nums:
            prod *= i

        def factorize(n):
            i = 2
            factors = set()
            while i * i <= n:
                while n % i == 0:
                    factors.add(i)
                    n = n // i
                i += 1
            if n > 1:
                factors.add(n)

            return factors
        
        return len(factorize(prod))

