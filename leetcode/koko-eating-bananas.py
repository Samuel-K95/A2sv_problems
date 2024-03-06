class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right

        while left <= right:
            mid = left + (right - left) // 2

            hr = 0
            for i in range(len(piles)):
                if piles[i] > mid:
                    hr += ceil((piles[i] / mid))
                else:
                    hr += 1

            if hr <= h:
                right = mid - 1
                best = mid
            else:
                left = mid + 1

        return best
            

