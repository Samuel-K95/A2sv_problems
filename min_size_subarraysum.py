class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        ans = float("inf")
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return ans if ans != float("inf") else 0
