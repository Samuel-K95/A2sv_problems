# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        collect = []
        n = len(s)

        for i in range(n):
            collect.append(abs(ord(s[i]) - ord(t[i])))
        
        mx_len = 0
        running = 0
        left = 0

        for right in range(n):
            running += collect[right]
            while running > maxCost:
                running -= collect[left]
                left += 1
            mx_len = max(mx_len, right - left + 1)

        return mx_len

