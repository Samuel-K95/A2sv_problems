class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        comp = [" " for i in range(len(s))]
        for i in range(len(s)):
            comp[int(s[i][-1]) - 1] = s[i][:-1]
        return " ".join(comp)
        