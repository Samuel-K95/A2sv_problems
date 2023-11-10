class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        beauty = 0
        l, r = 0, 0
        while r < len(str(num)):
            check = str(num)[l : r + 1]
            if r - l + 1 >= k:
                if r - l + 1 == k:
                    if int(check) != 0 and num % int(check) == 0:
                        beauty += 1
                l += 1

            r += 1
        return(beauty)