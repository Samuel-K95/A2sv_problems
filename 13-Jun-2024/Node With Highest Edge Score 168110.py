# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = defaultdict(int)
        m = 0
        
        for i in range(len(edges)):
            mp[edges[i]] += i
            m = max(m, edges[i])
        
        mx = float('-inf')
        idx = 0

        for i in range(m+1):
            if mp[i] > mx:
                idx = i
                mx = mp[i]

        return idx
