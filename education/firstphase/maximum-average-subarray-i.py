class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float("-inf")
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if((i - left) + 1 == k):
                ans = max(sum, ans)
                sum -= nums[left]
                left += 1
        return ans / k