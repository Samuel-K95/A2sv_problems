class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count  = Counter(nums)
        itera = len(nums) // 3
        ans = set()
        for i in nums:
            if count[i] > itera and i not in ans:
                ans.add(i)
        return list(ans)