class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = 0
        pointer = len(piles) - 2
        while pointer >= len(piles)// 3:
            mine += piles[pointer]
            pointer -= 2
        return mine
        