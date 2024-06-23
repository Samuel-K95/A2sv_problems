# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0]
        for i in nums:
            pref.append(pref[-1] + i)
        
        suff = [0]

        for i in range(len(nums)-1, -1, -1):
            suff.append(suff[-1] + nums[i])

        for i in range(len(nums)):
            pr = pref[i]
            suf = suff[len(suff)-i-2]

            if pr == suf:
                return i
        
        return -1


        