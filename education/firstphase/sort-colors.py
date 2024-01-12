class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i >= count[0] and i < count[0] + count[1]:
                nums[i] = 1
            elif i >= count[0] + count[1]:
                nums[i] = 2