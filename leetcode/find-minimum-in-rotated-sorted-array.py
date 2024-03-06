class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        targ = nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > targ:
                left = mid + 1
            else:
                right = mid - 1

        return nums[right + 1] if right + 1 < len(nums) else nums[0]
            
