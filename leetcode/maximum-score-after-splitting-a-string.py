class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        ans = 0
        zeros = 0
        for n in s[:-1]:
            if not int(n):
                zeros += 1
            ones -= int(n)
            ans = max(ans, ones + zeros)
        return ans

        