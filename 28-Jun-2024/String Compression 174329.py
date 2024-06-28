# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r=0,0
        track=0
        while r<len(chars):
            le=0
           
            while l<len(chars) and chars[l]==chars[r]:
                le+=1
                l+=1
            chars[track]=chars[r]
            track+=1
            if le>1:
                for u in str(le):
                    chars[track]=u
                    # l+=2
                    track+=1
            r=l
        for d in range(len(chars)-track):
            chars.pop()
       