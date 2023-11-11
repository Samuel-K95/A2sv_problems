class Solution:
    def reverseVowels(self, s: str) -> str:
        store = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left = 0
        right = len(s) - 1
        dup = list(s)
        while left <= right:
            if dup[left] in store:
                while right >= left:
                    if dup[right] in store:
                        dup[left], dup[right] = dup[right], dup[left]
                        break
                    right -= 1
                right -= 1
            left += 1
        return "".join(str(i) for i in dup)