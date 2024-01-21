class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(nums[i] + pref[-1])
        return pref