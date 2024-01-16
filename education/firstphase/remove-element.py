class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
            else:
                ans += 1
        j = 0
        for right in range(len(nums)):
            if nums[right] != '_':
                nums[j], nums[right] = nums[right], nums[j]
                j += 1
        return ans