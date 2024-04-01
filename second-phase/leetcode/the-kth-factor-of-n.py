class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def div(n):
            collect = []
            for i in range(1, int((n**0.5) + 1)):
                if n % i == 0:
                    collect.append(i)
                    if i != (n // i):
                        collect.append(n//i)
            return sorted(collect)
        arr = div(n)
        return arr[k-1] if k <= len(arr) else -1