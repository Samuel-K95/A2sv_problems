class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftprefix = []
        righprefix = []
        left = 0
        right = 0
        for i in range(len(nums)):
            left += nums[i]
            right += nums[len(nums) - 1 - i]
            leftprefix.append(left)
            righprefix.append(right)
        for i in range(len(nums)):
            if leftprefix[i] == righprefix[len(nums) - 1 - i]:
                return i
        return -1