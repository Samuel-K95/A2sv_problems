class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = x * -1
        ans = ""
        for i in range(len(str(x))):
            if str(x)[len(str(x)) - 1] == 0:
                continue
            else:
                ans += str(x)[len(str(x)) - 1 - i]

        if flag:
            ans = int(ans) * -1
            if -(2**31) <= int(ans):
                return int(ans)
            return 0

        else:
            if int(ans) <= (2**31) - 1:
                return ans
            return 0
