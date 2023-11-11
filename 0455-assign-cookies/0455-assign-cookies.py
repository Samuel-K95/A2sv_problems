class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s_point = 0
        count = 0
        g.sort()
        s.sort()
        for g_point in range(len(g)):
            while s_point < len(s) and g[g_point] > s[s_point]:
                s_point += 1
            if s_point < len(s) and g[g_point] <= s[s_point]:
                s_point += 1
                count += 1
        return count