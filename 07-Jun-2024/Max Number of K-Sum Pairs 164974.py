# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        track = Counter(nums)
        cnt = 0
        for i in range(len(nums)):
            curr = nums[i]
            ded = k - curr
            if track[curr] > 0:
                track[curr] -= 1
                if track[ded] > 0:
                    track[ded] -= 1
                    cnt += 1
                else:
                    track[curr] += 1
        return cnt
