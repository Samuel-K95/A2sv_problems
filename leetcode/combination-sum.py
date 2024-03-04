class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        vis = set()
        def backtrac(arr, tot):
            if tot > target:
                return
            if tot == target:
                arr = sorted(arr)
                dup  = tuple(arr) 
                if dup not in vis:
                    result.append(arr)
                    vis.add(dup)
            for j in range(len(candidates)):
                backtrac(arr+[candidates[j]], tot + candidates[j])

        backtrac([], 0)

        return result