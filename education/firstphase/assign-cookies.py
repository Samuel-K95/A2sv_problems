class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = 0
        size = 0
        s.sort()
        g.sort()
        count = 0
        while greed < len(g) and size < len(s):
            while size < len(s) and greed < len(g) and s[size] < g[greed]:
                size += 1
            if size < len(s) and greed < len(g) and s[size] >= g[greed]:
                count += 1
                greed += 1
                size += 1
            else:
                break
        return count

            