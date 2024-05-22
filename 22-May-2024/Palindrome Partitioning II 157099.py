# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        mem = {}

        def check_pal(l, r):
            t = s[l:r+1]
            rev = t[::-1]
            if t == rev:
                return True
            return False
        

        def track(idx):
            if idx >= len(s):
                return 0
            
            if (idx) not in mem:
                mem[idx] = float('inf')
                for i in range(idx, len(s)):
                    if check_pal(idx, i):
                        mem[idx] = min(mem[idx] ,1 + track(i+1))
            
            return mem[idx]
        
        return track(0)-1
            

            