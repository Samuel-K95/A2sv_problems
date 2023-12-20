class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                c += 1
            else:
                ans = max(ans, c)
                c = 0
        return max(ans, c)