# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # mem = {}
        # def top_down(val):
        #     if val <= 0:
        #         return 1 if val == 0 else 0
        #     if val not in mem:
        #         curr = 0
        #         for i in nums:
        #             curr += top_down(val-i)
        #         mem[val] = curr
            
        #     return mem[val]

        # return top_down(target)

        # bottom_up

        nums.sort()
        dp = [0 for _ in range(target + 1)] 
        dp[0] = 1

        for i in range(target+1):
            for val in nums:  
                if i + val < target+1:
                    dp[i+val] += dp[i]
        return dp[target]
