class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        second=0
        pos=1
        for i in range(1,len(piles), 3):
            second+=piles[pos]
            pos+=2
        return(second)