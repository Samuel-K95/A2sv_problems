# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        cnt = 0
        idx = 0
        rem = set()
        while n - len(rem) > 1:
            if idx not in rem:
                if cnt == k:
                    rem.add(idx)
                    cnt = 0
                cnt += 1
            idx += 1
            if idx > n:
                idx = 1
                    
        print(rem)
        while idx in rem:
            idx += 1
            if idx > n:
                idx = 1
        return idx if idx != 0 else n


            
        
