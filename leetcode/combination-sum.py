class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        vis = set()
        def backtrac(arr):
            if sum(arr) > target:
                return
            if sum(arr) == target:
                arr = sorted(arr)
                if tuple(arr) not in vis:
                    result.append(arr)
                    vis.add(tuple(arr))

            for j in range(len(candidates)):
                backtrac(arr+[candidates[j]])

        backtrac([])

        return result