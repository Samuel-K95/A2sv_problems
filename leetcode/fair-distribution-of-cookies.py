class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        small = float('inf')
        def backtrack(i, arr):
            nonlocal small
            if i >= len(cookies):
                large = max(arr)
                small = min(large, small)
                return
            
            for j in range(k):
                arr[j] += cookies[i]
                if arr[j] < small:
                    backtrack(i+1, arr)
                arr[j] -= cookies[i]
            
        arr = [0] * (k + 1)
        backtrack(0, arr)

        return small

