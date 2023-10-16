class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = [i for i in s]
        T = [i for i in t]
        S.sort()
        T.sort()
        return S == T
