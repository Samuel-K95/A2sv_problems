class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            num = str(num)
            num = [i for i in num]
            num.sort()
            left  = 0
            right = 0
            while right < len(num) and num[right] == '0':
                right += 1
            if right < len(num):
                num[left], num[right] = num[right], num[left]
            return int("".join(num))
        else:
            num = str(num)[1:]
            num = sorted(num, reverse= True)
            return -1 * int("".join(num))