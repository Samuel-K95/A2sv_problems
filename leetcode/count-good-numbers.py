class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        ans = 0
        if n % 2 == 0:
            even = n // 2
            odd = n // 2
        else:
            odd = n // 2
            even = n - odd
        
        ans = (pow(5, even, MOD)) * (pow(4, odd, MOD))
        return ans % MOD