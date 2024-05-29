# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # top_down 
        mem = {}
        def dp(idx, mask):
            if idx == len(nums1):
                return 0
            
            if (idx, mask) not in mem:
                small = float('inf')
                for i in range(len(nums2)):
                    if (1 << i) & mask == 0:
                        small = min(small, (nums1[idx] ^ nums2[i] )+ dp(idx + 1, 1 << i | mask))
                mem[(idx, mask)] = small

            return mem[(idx, mask)]
        
        return dp(0, 0)