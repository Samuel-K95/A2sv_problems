class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        right = 0
        final = 0
        tot = len(s)
        while right < tot:
            left = right
            count_first = 0
            while right < tot and s[right] == s[left]:
                right += 1
                count_first += 1
            left = right
            count_second = 0
            while right < tot and s[left] == s[right] and count_first > count_second:
                right += 1
                count_second += 1
            length = min(count_first, count_second)
            while length > 0:
                print(length)
                final += 1
                length -= 1
            right = left
        print(final, "final")
        return final


obj = Solution()
obj.countBinarySubstrings(s="00110")
