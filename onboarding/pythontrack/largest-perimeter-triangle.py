class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i+2]+ nums[i+1]+ nums[i]
        return 0