class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            curr = gcd(nums[i])
            if curr == k:
                count += 1
            for j in range(i+1, len(nums)):
                if gcd(nums[j], curr) == k:
                    count += 1
                curr = gcd(nums[j], curr)
        return count