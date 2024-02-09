class Solution:
    def minimumSteps(self, s: str) -> int:
        right = 0
        s = list(s)
        ans = 0
        zero = 0
        for right in range(len(s)):
            if s[right] == '0':
                s[zero], s[right] = s[right], s[zero]
                ans += (right - zero)
                zero += 1
        return ans

