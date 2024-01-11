class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        pref = 0
        count = 0
        ans = 0
        for i in range(len(flips)):
            pref += (i + 1)
            count += flips[i]
            if pref == count:
                ans += 1
        return ans