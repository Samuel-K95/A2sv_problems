# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        place = 0

        for seek in range(len(nums)):
            if nums[seek] > 0:
                nums[seek], nums[place] = nums[place], nums[seek]
                place += 1
        check = [0] * place

        for i in range(place):
            if nums[i] <= place:
                check[nums[i]-1] = 1
        
        for i in range(place):
            if check[i] == 0:
                return i + 1
        print(check)
        return place + 1