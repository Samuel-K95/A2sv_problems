class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        left = 0
        length = 0
        for right in range(len(s)):
            store[s[right]] = store.get(s[right], 0) + 1

            while left < len(s) and store[s[right]] > 1:
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]
                left += 1
            length = max(length, right - left + 1)

        return length