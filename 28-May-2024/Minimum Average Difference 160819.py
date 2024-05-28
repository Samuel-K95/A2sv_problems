# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref = [nums[0]]
        n = len(nums)
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
        
        ans = []

        for i in range(len(nums)):
            left = pref[i] // (i + 1)

            right = (pref[-1] - pref[i]) // (n - i - 1) if n - i - 1 > 0 else 0

            ans.append(abs(left - right))
        idx = 0

        for i in range(len(ans)):
            if ans[i] < ans[idx]:
                idx = i
                
        return idx