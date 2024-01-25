class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        store = Counter(nums)
        if store[0] > 1:
            return [0] * len(nums)
        elif store[0] == 1:
            mult = 1
            ans = []
            pos = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    mult *= nums[i]
                else:
                    pos = i
                ans.append(0)
                
            ans[pos] = mult
            return ans
        else:
            mult = 1
            for val in nums:
                mult *= val
            ans = []
            for j in range(len(nums)):
                ans.append(mult // nums[j])
            return ans

            