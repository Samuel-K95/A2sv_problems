class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        vis = defaultdict(int)
        candidates.sort()

        def backtrack(arr, tot, i):
            if i > len(candidates):
                return
            if tot > target:
                return

            if tot == target:
                ans.append(arr)
                return

            before = 0

            for j in range(i, len(candidates)):
                if candidates[j] == before:
                    continue
                backtrack(arr + [candidates[j]], tot + candidates[j], j+1)
                before = candidates[j]

        backtrack([], 0, 0)
        return ans