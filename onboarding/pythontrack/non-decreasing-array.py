class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        op = 0
        for i in range(len(nums)- 1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                if i ==  0 or nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                op += 1
        print(nums)
        if op > 1:
            return False
        else:
            return True




             