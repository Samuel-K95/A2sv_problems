class Solution:
    def isHappy(self, n: int) -> bool:
        checker = set()
        while True:
            tot = 0
            n = str(n)
            for i in range(len(n)):
                tot += int(n[i]) ** 2
            if tot == 1:
                return True
            if tot in checker:
                break
            checker.add(tot)
            n = tot
        return False