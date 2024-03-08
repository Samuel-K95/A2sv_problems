class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted([i for i in nums if i > 0])
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                targ = bisect_left(nums, nums[i]+ nums[j])
                count += targ - j - 1
        return count

