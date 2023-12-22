class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        store = zip(s, indices)
        ret = sorted(store, key = lambda x : x[1])
        ans = []
        for i in ret:
            ans.append(i[0])
        return "".join(ans)
