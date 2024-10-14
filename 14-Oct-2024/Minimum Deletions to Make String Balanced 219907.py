# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        pref = [0]

        for i in range(len(s)):
            if s[i] == 'b':
                pref.append(pref[-1] + 1)
            else:
                pref.append(pref[-1])
            
        suff = [0]
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'a':
                suff.append(suff[-1] + 1)
            else:
                suff.append(suff[-1])
        
        suff.reverse()
        ans = float(inf)

        for i in range(len(pref)):
            ans = min(pref[i] + suff[i], ans)

        return ans

            