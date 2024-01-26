class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ref = [0] * len(s)
        change={0:-1, 1:1}
        for i in shifts:
            ref[i[0]] += change[i[2]]
            if i[1] + 1 < len(s):
                ref[i[1] + 1] -= change[i[2]]
        for i in range(1, len(ref)):
            ref[i] += ref[i-1]
        ans = []
        for i in range(len(ref)):
            change = ord(s[i]) + ref[i]
            while change > 122:
                change = 96 + (change - 122)
            while change < 97:
                change = 123 - (97 - change)
            ans.append(chr(change))
        return "".join(ans)