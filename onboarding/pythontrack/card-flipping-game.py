class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        check = defaultdict(bool)
        cant = set()
        ans = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cant.add(fronts[i])
                if fronts[i] in ans:
                    ans.discard(fronts[i])
            else:
                if fronts[i] not in cant:
                    ans.add(fronts[i])
                if backs[i] not in cant:
                    ans.add(backs[i])
        ans = sorted(ans)
        return ans[0] if ans != [] else 0
