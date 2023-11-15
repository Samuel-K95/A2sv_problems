class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        flips = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flips += 1

            if flips <= k:
                res = max(res, right - left + 1)
            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1
        return res
