# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        check = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            l_most = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if l_most + nums[left] + nums[right] > 0:
                    right -= 1
                elif l_most + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    curr = (l_most, nums[left], nums[right])
                    if curr not in check:
                        ans.append([l_most, nums[left], nums[right]])
                        check.add(curr)
                    left += 1
                    right -= 1
        return ans
                    

