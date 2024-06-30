# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        neg = set()
        pos = set()
        row = set()
        col = set()
        count = 0

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return
            
            for j in range(n):
                if (j in col) or (r + j in neg) or ( r - j in pos):
                    continue
                
                col.add(j)
                neg.add(r+j)
                pos.add(r-j)

                backtrack(r + 1)
                    
                col.remove(j)
                neg.remove(r+j)
                pos.remove(r-j)

            return
        
        backtrack(0)
        print(row)
        print(col)
        print(neg)
        print(pos)


        return count
    


                    