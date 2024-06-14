# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnt = 0
        ans = []
        n = len(nums)

        nums.sort()
        for i in range(n):
            add = 0
            if ans:
                top = ans[-1]
                if top >= nums[i]:
                    add = (top - nums[i]) + 1
            ans.append(nums[i] + add)
            cnt += add
        
        return cnt
