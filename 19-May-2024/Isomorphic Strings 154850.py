# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mps = defaultdict(str)
        mpt = defaultdict(str)

        for i in range(len(t)):
            if s[i] in mps:
                if mps[s[i]] != t[i]:
                    return False
            elif t[i] in mpt:
                if mpt[t[i]] != s[i]:
                    return False
            else:
                mps[s[i]] = t[i]
                mpt[t[i]] = s[i]

        return True