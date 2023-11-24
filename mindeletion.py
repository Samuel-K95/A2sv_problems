class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        left = 0
        right = left + 1
        l = len(nums)
        operation = 0
        k = 0
        while left < l and right < l:
            while left < l and right < l and k % 2 == 0 and nums[right] == nums[left]:
                operation += 1
                right += 1
            left = right
            right += 1
            k += 1
        if (l - operation) % 2 == 0:
            return operation
        else:
            return operation + 1
