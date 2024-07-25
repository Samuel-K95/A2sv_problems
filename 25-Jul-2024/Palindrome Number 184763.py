# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        left = 0
        right = len(str_x)-1

        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        
        return True