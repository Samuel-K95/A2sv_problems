# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        store = defaultdict(list)
        for i in range(len(nums)):
            store[nums[i]].append(i)

        fin = [0] * len(nums)
        for j in (store):
            arr = store[j]
            tot = 0
            for i in range(1, len(arr)):
                tot += arr[i] - arr[0]

            fin[arr[0]] = tot

            for i in range(1, len(arr)):
                tot  += (arr[i] - arr[i-1]) * (i + 1)
                tot -= (arr[i] - arr[i-1]) * (len(arr) - (i-2) -1)
                fin[arr[i]] = tot
        return fin
