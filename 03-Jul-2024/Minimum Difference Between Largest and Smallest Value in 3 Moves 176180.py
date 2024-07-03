# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) > 3:
            fir = nums[-4] - nums[0]
            sec = nums[-1] - nums[3]
            thir = nums[-2] - nums[2]
            four = nums[-3] - nums[1]
            return min(fir, sec, thir, four) 
        else:
            return 0 