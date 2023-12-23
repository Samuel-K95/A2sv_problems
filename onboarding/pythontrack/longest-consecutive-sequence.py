class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        length=0
        for i in nums:
            if (i-1) not in numset:
                start=0
                while(i+start) in numset:
                    start+=1
                length=max(start, length)
        return(length)