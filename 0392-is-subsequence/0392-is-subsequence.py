class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small = 0
        temp = 0
        count = 0
        for small in range(len(s)):
            while temp < len(t) and t[temp] != s[small]:
                temp += 1

            if temp < len(t) and t[temp] == s[small]:
                t = t[:temp] + t[temp+1:]
                count += 1
        return count == len(s)

                

            