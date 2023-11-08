class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res  = float('-inf')
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while right - left + 1 >k:
                current_sum -= nums[left]
                left += 1
            if right - left + 1 == k:
                res = max(res,current_sum)
        return res / k