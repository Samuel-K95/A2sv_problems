class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left <= right:
            while left < len(s) and ((ord(s[left]) > 122 or ord(s[left]) < 97) and (ord(s[left]) < 48 or ord(s[left]) > 57)):
                left += 1
            while right > 0 and  ((ord(s[right]) > 122 or ord(s[right]) < 97) and (ord(s[right]) < 48 or ord(s[right]) > 57)):
                right -= 1
            if left <= right:
                if s[left] != s[right]:
                    print(left, s[left], right, s[right])
                    return False
            left += 1
            right -= 1
        return True