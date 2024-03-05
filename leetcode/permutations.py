class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(arr, i):
            if i == len(nums):
                return  [[]]
            

            result = []
            permutations = backtrack(arr, i+1)

            for p in permutations:
                for j in range(len(p) + 1):
                    copyp = p[:]
                    copyp.insert(j, nums[i])
                    result.append(copyp)
                    
            return result
        
        return backtrack(nums, 0)

