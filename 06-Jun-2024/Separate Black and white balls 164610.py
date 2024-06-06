# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        placeholder = 0
        s = [i for i in s]
        ans = 0
        for seeker in range(len(s)):
            if s[seeker] == '0':
                ans += (seeker - placeholder)
                s[seeker], s[placeholder] = s[placeholder], s[seeker]
                placeholder += 1
        
        return ans