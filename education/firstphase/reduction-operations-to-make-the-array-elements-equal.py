class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        answer = []
        same = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                same += 1
            else:
                answer.append(same)
                same = answer[-1] + 1
        return sum(answer)

