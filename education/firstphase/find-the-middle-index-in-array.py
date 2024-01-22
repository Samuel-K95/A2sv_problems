class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref = [0]
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])
        nums.reverse()
        rever = [0]
        for i in range(len(nums)):
            rever.append(rever[-1] + nums[i])
        rever.reverse()
        for i in range(len(nums)):
            if pref[i] == rever[i + 1]:
                return (i)
        return -1