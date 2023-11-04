class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        k = len(needle)
        while left < len(haystack):
            right = 0
            while (
                right < len(needle)
                and left + right < len(haystack)
                and haystack[left + right] == needle[right]
            ):
                right += 1
            if right == k:
                return left
            left += 1
        return -1