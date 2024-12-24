# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        ans = float('inf')
        left = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum >= target:
                ans = min(ans, right-left + 1)
                running_sum -= nums[left]
                left += 1
        
        if ans == float('inf'):
            ans = 0

        return ans