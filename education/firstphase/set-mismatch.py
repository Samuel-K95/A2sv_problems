class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep = Counter(nums)
        nums.sort()
        dup, mis = 0, 0
        for i in range(len(nums)):
            if i + 1 not in rep:
                mis = i+1
            if rep[nums[i]] == 2:
                dup = nums[i]
        return [dup, mis]
        
        