class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = defaultdict(list)
        left = 0
        right = Counter(nums)
        ans = []
        highest = float('-inf')
        for i  in range(0, len(nums) + 1):
            if i == 0:
                sums = right[1]
            else:
                if nums[i-1] == 0:
                    left += 1
                else:
                    right[1] -= 1
                sums = left + right[1]
            highest = max(highest, sums)
            ans.append(sums)
        fin = []
        for i in range(len(ans)):
            if ans[i] == highest:
                fin.append(i)
        return fin
            
