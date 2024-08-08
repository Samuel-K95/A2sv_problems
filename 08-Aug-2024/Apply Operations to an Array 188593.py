# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        placeholder = 0
        for seeker in range(n):
            if nums[seeker] != 0:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                placeholder += 1
        
        return nums
