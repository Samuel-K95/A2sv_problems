class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot = 0
        prefix = []
        for i in range(len(nums)):
            tot += nums[i]
            prefix.append(tot)
        return prefix