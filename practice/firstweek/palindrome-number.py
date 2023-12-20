class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = 0
        r = len(str(x))-1
        wor = str(x)
        while l <= r:
            if wor[l] != wor[r]:
                return False
            l += 1
            r -= 1
        return True
            