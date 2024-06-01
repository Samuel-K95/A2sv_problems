# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        taken = 0
        target = sum(nums) // k
        nums.sort(reverse=True)
        mem = {}

        def dp(idx, k, curr_sum):
            nonlocal taken, target
            if k == 0:
                return True

            if curr_sum == 0:
                return dp(0, k-1, target)
            
            if (taken, k) not in mem:
                curr = False
                for i in range(idx, len(nums)):
                    if ((1 << i) & taken) > 0 or curr_sum - nums[i] < 0:
                        continue
                    taken = taken | (1 << i)
                    if dp(i + 1, k, curr_sum - nums[i]):
                        curr = True
                        break
                    taken = taken ^ (1 << i)

                mem[(taken, k)] = curr

            return mem[(taken, k)]

        if sum(nums) % k:
            return False
        
        return dp(0, k, target)
