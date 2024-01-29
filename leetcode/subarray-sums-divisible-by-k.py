class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        store = defaultdict(int)
        pref = 0
        store[0] += 1
        for i in range(len(nums)):
            pref += nums[i]
            if pref % k in store:
                ans += store[pref % k]
            store[pref % k] += 1
        return ans