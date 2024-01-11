class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # similar approach with three sum but since the target can not be found from the sum of the elements, 
        # we would store the smallest interval for each combination, and finally return it

        #the curr pointer would iterate through the array and 
        nums.sort()
        pick, curr_coll = float('inf'), tuple()
        for curr in range(len(nums)):
            left = curr + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[curr] + nums[left] + nums[right]
                if abs(target-current_sum) < pick:
                    pick = abs(target-current_sum)
                    curr_coll = (nums[curr], nums[left], nums[right])
                if nums[curr] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return sum(curr_coll)


