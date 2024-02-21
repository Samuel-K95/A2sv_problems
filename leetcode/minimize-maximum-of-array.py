class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        currMax = nums[0]
        pref = nums[0]
        for i in range(1, len(nums)):
            pref += nums[i]
            if nums[i] > currMax:
                currMax = max(currMax,math.ceil( pref / (i + 1)))
        return (currMax)


