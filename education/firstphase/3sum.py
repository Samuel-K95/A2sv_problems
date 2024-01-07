class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        vis = set()
        for i in range(len(nums)):
            curr = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if curr + nums[left] + nums[right] < 0:
                    left += 1
                elif curr + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    pot = (curr,nums[left], nums[right])
                    if pot not in vis:
                        ans.append([curr,nums[left], nums[right]])
                        vis.add((curr,nums[left], nums[right]))
                    left += 1
                    right -= 1
        return ans