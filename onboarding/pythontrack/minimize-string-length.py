class Solution:
    def delleft(self, i: int, s: list, t: str):
        while i >= 0:
            if s[i] == t:
                return i
            i -= 1
        return -1

    def delright(self, i: int, s:list, t:str):
        while i < len(s):
            if s[i] == t:
                return i
            i += 1
        return -1

    def minimizedStringLength(self, s: str) -> int:
        s=[i for i in s]
        full = len(s)
        for i in range(len(s)):
            left = self.delleft(i-1, s, s[i])
            right = self.delright(i+1, s, s[i])
            if left != -1:
                s[left] = ""
                full -= 1
            if right != -1:
                s[right] = ""
                full -= 1
        s="".join(s)
        print(s)
        return len(s)        