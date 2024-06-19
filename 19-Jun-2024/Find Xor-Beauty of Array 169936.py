# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        coll = 0

        for i in range(len(nums)):
            coll ^= nums[i]
        
        return coll
