class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup = ""
        for i in s:
            if i.isalnum():
                if i == " ":
                    continue
                dup += i.lower()
        num = len(dup) - 1

        for i in range(len(dup)):
            if dup[i] != dup[num - i]:
                return False
        return True
