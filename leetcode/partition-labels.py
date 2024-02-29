class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = defaultdict(int)

        for i in range(len(s)):
            last_occ[s[i]] = i
        
        l = 0
        ans = []
        comp = 0
        for r in range(len(s)):
            comp = max(comp,  last_occ[s[r]])
            if r == comp:
                ans.append(r - l + 1)
                l = r + 1
        return ans