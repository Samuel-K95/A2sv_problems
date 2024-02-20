class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = Counter(s)
        odd = 0
        ans = 0
        for i in check:
            if check[i] % 2 == 0:
                ans += check[i]
            else:
                ans += (check[i] - 1)
                odd += 1
        return ans if odd == 0 else ans + 1

