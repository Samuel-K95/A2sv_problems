class Solution:
    def climbStairs(self, n: int) -> int:
        # @lru_cache(None)
        # def fib(a):
        #     if a <= 1:
        #         return 1
        #     else:
        #         return fib(a-1) + fib(a-2)
        # return fib(n)
        store = defaultdict(int)
        store[1] = 1
        store[2] = 2
        for i in range(3, n + 1):
            store[i] = store[i-1] + store[i-2]
        return store[n]