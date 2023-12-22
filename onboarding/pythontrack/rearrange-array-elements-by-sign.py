class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        index = 0
        for i in range(0, len(nums), 2):
            nums[i] = pos[index]
            nums[i+1] = neg[index]
            index += 1
        return nums

            

            
