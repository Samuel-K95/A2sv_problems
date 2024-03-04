class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        store = []

        def backtrack(arr, i):
            store.append(arr)

            for j in range(i, len(nums)):
                backtrack(arr + [nums[j]], j+1)

            return

        backtrack([], 0)

        return store