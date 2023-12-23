class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        val = 0
        for i in range(len(nums)):
            if nums[i] != val:
                return val
            val += 1
        return val
        