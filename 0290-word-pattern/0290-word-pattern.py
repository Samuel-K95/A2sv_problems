class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash = {}
        hash_1 = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i, val in enumerate(pattern):
            if val in hash or s[i] in hash_1:
                if val in hash:
                    if s[i] != hash[val]:
                        return False
                else:
                    if hash_1[s[i]] != val:
                        return False
            else:
                hash[val] = s[i]
                hash_1[s[i]] = val
        return True