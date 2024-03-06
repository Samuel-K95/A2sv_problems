class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            counter = 0
            calc_days = 1

            for i in range(len(weights)):
                counter += weights[i]
                if counter > mid:
                    calc_days += 1
                    counter = weights[i]
            
            if calc_days > days:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid

        return ans
