class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr = defaultdict(int)
        for i in range(len(bills)):
            curr[bills[i]] += 1
            while 10 in curr and bills[i] > 10:
                bills[i] -= 10
                curr[10] -= 1
                if curr[10] <= 0:
                    del curr[10]
            while 5 in curr and bills[i] > 5:
                bills[i] -= 5
                curr[5] -= 1
                if curr[5] <= 0:
                    del curr[5]
            if bills[i] > 5:
                return False
        return True

