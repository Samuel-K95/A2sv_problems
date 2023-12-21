class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        dup = list(s)
        if k > len(dup):
            dup.reverse()
            return "".join(str(i) for i in dup)
        for i in range(len(s)):
            if i % (2 * k) == 0:
                left = i
                right = i + k - 1 if i + k - 1 < len(dup) else len(dup) - 1
                while left <= right:
                    dup[left], dup[right] = dup[right], dup[left]
                    left += 1
                    right -= 1
        return "".join(str(i) for i in dup)
                    