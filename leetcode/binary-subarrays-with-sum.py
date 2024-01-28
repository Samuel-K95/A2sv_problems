class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        store = defaultdict(int)
        ans = 0
        pref = 0
        store[0] += 1
        for i in range(len(nums)):
            pref += nums[i]
            if pref - goal in store:
                ans += store[pref-goal]
            store[pref] += 1
        return ans