class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                continue
            
            elements = math.ceil(nums[i] / nums[i+ 1])
            count += (elements - 1)
            lower = nums[i] // (elements)
            nums[i] = lower
        
        return count