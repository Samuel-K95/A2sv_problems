class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                if left == 0:
                    count += 1
                else:
                    if left != 0:
                        left -= 1
        return count + left