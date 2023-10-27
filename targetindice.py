class Solution:
    def targetIndices(self, nums: list[int], target: int) -> List[int]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        answer.sort()
        return answer
