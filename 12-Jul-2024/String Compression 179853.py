# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        place = 0
        right = 0
        n = len(chars)
        ans = 0
        while right < len(chars):
            curr = chars[right]
            cnt = 0
            while right < n and chars[right] == curr:
                right += 1
                cnt += 1

            chars[place] = curr
            ans += 1
            place += 1
            if cnt > 1:
                for i in range(len(str(cnt))):
                    ans += 1
                    chars[place] = str(cnt)[i]
                    place += 1
        return ans

        
       