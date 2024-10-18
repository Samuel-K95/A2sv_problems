# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        store = []

        def backtrack(idx, arr):
            if idx == len(nums):
                store.append(arr)
                return 
            if arr:
                store.append(arr)
            for i in range(idx, len(nums)):
                backtrack(i + 1, arr + [nums[i]])
            
            return
        
        backtrack(0, [])
        temp = defaultdict(int)
        for arr in store:
            bit_or = 0
            for val in arr:
                bit_or |= val
            temp[bit_or] += 1

        return max(temp.values())
        