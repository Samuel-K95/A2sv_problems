class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        best = 0

        while left <= right:
            mid = left + (right - left) // 2

            part = 0
            curr = 0
            max_sum = 0
            for i in range(len(nums)):
                if curr + nums[i] > mid:
                    part += 1
                    curr = nums[i]
                else:
                    curr += nums[i]

            part += 1

            if part > k:
                left = mid + 1
            else:
                best = mid
                right = mid - 1

        return best

                