class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        tmp = 0
        left = 0
        for right in range(len(nums)):
            if tmp < 0:
                tmp = 0
            tmp += nums[right]
            ans = max(ans, tmp)
        return ans