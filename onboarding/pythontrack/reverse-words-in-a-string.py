class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.strip()
        s=s.split()
        s.reverse()
        fin = []
        for i in range(len(s)):
            if type(s[i]) == str:
                fin.append(s[i])
                if i != len(s)-1:
                    fin.append(" ")
        return "".join(fin)