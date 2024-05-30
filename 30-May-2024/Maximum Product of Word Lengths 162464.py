# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mem = {}
        def dp(n, idx, prev):
            if n == 2:
                return 1
            if idx == len(words):
                return 0
            
            if (idx, prev) not in mem:
                flag = True
                collect = 0
                for i in words[idx]:
                    curr = (1 << (ord(i) - ord('a')))
                    if curr & prev:
                        flag = False
                    else:
                        collect = collect | curr
                take = 0
                if flag:
                    take = len(words[idx]) * dp(n + 1, idx + 1, prev | collect)

                not_take = dp(n, idx+1, prev)

                mem[(idx, prev)] = max(take, not_take)

            return  mem[(idx, prev)]
        

        return dp(0, 0, 0)
        





