class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        check = Counter(nums)
        curr = defaultdict(int)
        ans = 0
        left = 0
        for right in range(len(nums)):
            curr[nums[right]] += 1
            while len(curr) == len(check):
                curr[nums[left]] -= 1
                if curr[nums[left]] == 0:
                    del curr[nums[left]]
                left += 1
                ans += len(nums) - right
        return ans


