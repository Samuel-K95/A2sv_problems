class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])
        nums.reverse()
        suffix= [0]
        for i in range(len(nums)):
            suffix.append(suffix[-1] + nums[i])
        suffix.reverse()
        nums.reverse()
        ans = []
        for i in range(len(nums)):
            left = (nums[i] * i) - pref[i]
            right = suffix[i] - (nums[i] * (len(suffix) - i - 1))
            ans.append(left + right)
        return ans
