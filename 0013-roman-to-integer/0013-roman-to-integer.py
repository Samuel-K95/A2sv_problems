class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        l = 0
        r = 1
        while l < len(s):
            if l < len(s) - 1 and symbol[s[r]] > symbol[s[l]]:
                ans += symbol[s[r]] - symbol[s[l]]
                if (r + 2) < len(s):
                    r += 2
                else:
                    r += 1
                l += 2
            else:
                ans += symbol[s[l]]
                r += 1
                l += 1
        return ans