class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dup = nums + nums
        stack = []
        ans = [-1] * (len(dup))
        for i in range(len(dup)):
            while stack and stack[-1][0] < dup[i]:
                ans[stack[-1][1]] = dup[i]
                stack.pop()
            stack.append([dup[i], i])
        return ans[:len(nums)]

            

