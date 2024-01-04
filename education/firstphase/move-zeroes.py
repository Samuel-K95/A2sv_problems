class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums)):
            right = left
            while right < len(nums) and nums[left] == 0 and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
        

        