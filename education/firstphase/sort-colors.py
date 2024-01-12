class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        c = 0
        for i in range(len(nums)):
            if c < count[0]:
                nums[i] = 0
            elif c >= count[0] and c < count[0] + count[1]:
                nums[i] = 1
            elif c >= count[0] + count[1]:
                nums[i] = 2
            c += 1