class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = curr_sum = 0
        store = defaultdict(int)
        for right in range(len(nums)):
            curr_sum += nums[right]
            store[nums[right]] += 1
            while  store[nums[right]] > 1:
                curr_sum -= nums[left]
                store[nums[left]] -= 1
                left += 1
            ans = max(ans, curr_sum)
        return ans