class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        store = defaultdict(list)
        for i in range(len(nums)):
            store[nums[i]].append(i)

        ans = [0] * len(nums)
        for j in (store):
            arr = store[j]
            tot = 0
            for i in range(1, len(arr)):
                tot += arr[i] - arr[0]

            ans[arr[0]] = tot

            for i in range(1, len(arr)):
                tot  += (arr[i] - arr[i-1]) * (i + 1)
                tot -= (arr[i] - arr[i-1]) * (len(arr) - (i-2) -1)
                ans[arr[i]] = tot
        return ans
