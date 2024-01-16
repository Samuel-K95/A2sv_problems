class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0
        ans = 0
        ded = {0:1, 1:0}
        for right in range(len(nums)):
            if nums[right] == 0 and count <= 1:
                count += 1
            while left < len(nums) and count > 1:
                count -= ded[nums[left]]
                left += 1
            ans = max(ans, right - left)
        if ans == len(nums):
            ans -= 1
        return ans
