class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = 0
        maximum = float('-inf')
        left = 0
        if len(nums) == 1:
            return nums[0]
        for right in range(len(nums)):
            if right + 1 - left > k:
                window -= nums[left]
                left += 1
            window += nums[right]
            if right - left + 1 == k:
                maximum = max(window, maximum)
        return maximum / k