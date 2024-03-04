class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        store = []
        vis = set()
        def backtrack(arr, i):
            li = sorted(arr)
            if tuple((li)) not in vis:
                vis.add(tuple(li))
                store.append(li)

            for j in range(i, len(nums)):
                backtrack(arr + [nums[j]], j+1)

            return

        backtrack([], 0)

        return store