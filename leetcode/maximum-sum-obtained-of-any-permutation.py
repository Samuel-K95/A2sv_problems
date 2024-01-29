class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        store = [0] * len(nums)
        for i in range(len(requests)):
            store[requests[i][0]]+= 1
            if requests[i][1]+ 1 < len(nums):
                store[requests[i][1] + 1] -= 1
        for i in range(1, len(store)):
            store[i] += store[i-1]
        store.sort()
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            ans += (nums[i] * store[i])
        return ans % (10 ** 9 + 7)