# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        first = defaultdict(int)
        second = defaultdict(int)

        fir, sec = 0, 0
        while fir < len(s) and sec < len(t):
            if s[fir] not in first and t[sec] not in second:
                first[s[fir]] = t[sec]
                second[t[sec]] = s[fir]
            else:
                if first[s[fir]] != t[sec]:
                    return False
                
                if second[t[sec]] != s[fir]:
                    return False
            fir += 1
            sec += 1
        
        if fir < len(s):
            return False
        
        if sec < len(t):
            return False
        
        return True