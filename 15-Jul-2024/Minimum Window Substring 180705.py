# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        final = float('inf')

        check = len(t)
        count = 0
        t_count = Counter(t)
        final_right = 0
        store = defaultdict(int)
        final_left = 0

        for right in range(len(s)):
            store[s[right]] += 1
            if store[s[right]] <= t_count[s[right]]:
                count += 1
            while left < len(s) and  count == check:
                if right - left + 1 < final:
                    final_left = left
                    final_right = right
                    
                    final = right - left + 1
                if s[left] in t_count and store[s[left]] == t_count[s[left]]:
                    count -= 1                    
                store[s[left]] -= 1
                left += 1
            
        if final != float('inf'):
            return s[final_left:final_right+1]
        return ""                