class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def backtrack(n, s, k):
            if n == 0:
                return s
            
            mid = pow(2 , n) // 2

            if k > mid:
                k -= mid
                if s == 0:
                    return backtrack(n-1, 1, k)
                else:
                    return backtrack(n-1, 0, k)
            else:
                if s == 0:
                    return backtrack(n-1, 0, k)
                else:
                    return backtrack(n-1, 1, k)

        return backtrack(n, 0, k)
