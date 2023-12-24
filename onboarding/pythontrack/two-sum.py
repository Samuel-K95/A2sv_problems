class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}

        for i in range(len(nums)):
            if nums[i] in store.values():
                return (nums.index(target - nums[i]), i)
            store.setdefault(i, target - nums[i])
                
            

