class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        check = 0
        i = 0
        for j in range(len(nums) - 1):
            if nums[i] + i >= len(nums) - 1:
                return True
            check = max(check, i + nums[i])
            if check > i:
                i += 1
        return False
            
            
            
        