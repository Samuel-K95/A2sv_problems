class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = list(num)
        ans = float('inf')
        for i in range(len(num)):
            if int(num[i]) %2  != 0:
                ans = i
        return "".join(num[:ans+1]) if ans != float('inf') else ""
            
        