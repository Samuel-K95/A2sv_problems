class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pref = 0
        ans = 0
        track = defaultdict(int)
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            diff = count[1]-count[0]
            if diff not in track:
                track[diff] = i 
            if count[1] == count[0]:
                ans = max(ans, count[1] + count[0])
            else:
                ans = max(ans, i - track[diff])
            
        return ans