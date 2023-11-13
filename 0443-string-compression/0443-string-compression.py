class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        left = 0
        while left < len(chars):
            count = 0
            place_holder = chars[left]
            while left <len(chars) and chars[left] == place_holder:
                left += 1
                count += 1
            ans += place_holder
            if count > 1:
                ans += str(count)
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)