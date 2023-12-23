class Solution:
    def totalMoney(self, n: int) -> int:
        tot = 0
        c = 1
        for i in range(1, n+1):
            tot += c
            if i % 7 == 0:
                c = i / 7
            c += 1
        return int(tot)
