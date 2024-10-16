# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def compute(n, p):
            vals = 1
            while p:
                if p & 1:
                    vals *= n
                
                n *= n
                p >>= 1
            
            return vals
        
        val = compute(x, abs(n))
        if n < 0:
            val = 1 / val
        
        return val

            

                


