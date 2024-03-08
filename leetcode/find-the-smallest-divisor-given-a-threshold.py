class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left = 1
        right = nums[-1]
        best = 0

        while left <= right:
            mid = left + (right - left) // 2

            tot = 0
            for i in nums:
                curr = ceil(i / mid)
                tot += curr
            
            if tot > threshold:
                left = mid + 1
            else:
                best = mid
                right = mid - 1

        return best 
