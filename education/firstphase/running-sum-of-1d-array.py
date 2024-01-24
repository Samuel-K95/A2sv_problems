class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = [nums[0]]
        for i in range(1, len(nums)):
            running.append(nums[i] + running[-1])
        return running