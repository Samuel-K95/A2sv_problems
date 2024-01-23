class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0 
        ans = 0
        store = defaultdict(int)
        store[0] += 1
        for i in range(len(nums)):
            pref += nums[i]
            if pref - k in store:
                ans += store[pref- k]
            store[pref] += 1
        return ans
        



