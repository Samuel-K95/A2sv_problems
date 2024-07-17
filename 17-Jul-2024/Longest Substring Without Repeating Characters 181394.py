# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        ans = 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
