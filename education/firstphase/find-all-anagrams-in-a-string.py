from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        store = {}
        count = Counter(p)
        left = 0
        length  = len(p)
        if(length > len(s)): return []
        ans = []
        for i in range(len(s)):
            if(s[i] in store):
                store[s[i]] += 1
            else: 
                store[s[i]] = 1
            
            if(length == (i - left) + 1):
                if store == count:
                    ans.append(left)
                store[s[left]] -= 1
                if store[s[left]]  == 0:
                    del store[s[left]]
                left += 1
        return ans