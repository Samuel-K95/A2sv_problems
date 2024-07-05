# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        fibs = [_ for _ in range(n+1)]
        for i in range(2, n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]
        return fibs[-1]
        