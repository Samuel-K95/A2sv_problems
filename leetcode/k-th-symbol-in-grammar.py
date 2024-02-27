class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def recur(n, s, k):
            if n == 1:
                if s == 0:
                    if k == 1:
                        return 0
                    else:
                        return 1
                else:
                    if k == 1:
                        return 1
                    else:
                        return 0
            curr = (2 ** (n - 1)) // 2

            if curr >= k:
                return recur(n -1, s, k)
            else:
                s = 1-s
                return recur(n-1, s, k - curr)

        return recur(n, 0, k)
