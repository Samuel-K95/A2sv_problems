class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)

        targ = tot % p
        if targ == 0:
            return 0
        store= defaultdict(int)
        pref = 0
        store[0] = -1
        ans = float('inf')
        for i in range(len(nums)):
            pref  = (pref + nums[i])  % p
            if( pref - targ)%p in store:
                ans = min(ans, i - store[(pref- targ)%p])
            store[pref] = i
        return ans if ans < len(nums) else -1