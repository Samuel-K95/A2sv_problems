class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(len(s)):
                curr = s[i:j + 1]
                low = curr.lower()
                if len(set(curr) )// 2 == len(set(low)):
                    if len(curr) > len(ans):
                        ans = curr
        return ans