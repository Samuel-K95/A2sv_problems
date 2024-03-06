class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        left, right = 0, max(houses[-1], heaters[-1])
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            i,j = 0, 0

            while i < len(heaters) and j < len(houses):
                if abs(heaters[i] - houses[j]) <= mid:
                    j += 1
                else:
                    i += 1

            if j >= len(houses):
                right = mid - 1
            else:
                left = mid + 1

        return left