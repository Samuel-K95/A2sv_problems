class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]

        for i in nums:
            if i in ans:
                continue
            else:
                ans.append(i)
        for i in range(len(ans)):
            nums[i]=ans[i]
        return(len(ans))
