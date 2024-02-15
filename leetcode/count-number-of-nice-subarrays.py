class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count += 1
            if (count - k) in store:
                ans += store[count - k]
            store[count] += 1
        return ans
