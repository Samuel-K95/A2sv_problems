class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        flag = True
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                flag = False
                break
        if not flag:
            return "".join(palindrome)
        else:
            palindrome[-1] = 'b'
            return "".join(palindrome)

                 

