class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(arr, c):
            if len(arr) == k:
                ans.append(arr)
                return
            
            for i in range(c, n +1):
                backtrack(arr + [i], i+1)


        backtrack([], 1)

        return ans
            