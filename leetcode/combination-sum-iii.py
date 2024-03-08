class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def bactrack(tot, arr, i):
            if tot == n and len(arr) == k:
                ans.append(arr)
                return
            
            if tot > n or len(arr) > k or i > n:
                return
            
            for j in range(i, 10):
                bactrack(tot + j, arr + [j], j+1)
            

        bactrack(0, [], 1)

        return ans
