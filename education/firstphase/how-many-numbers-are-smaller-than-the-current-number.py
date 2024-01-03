class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store = defaultdict(int)
        dup = [i for i in nums]
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i] not in store:
                store[nums[i]] = i

        for i in dup:
            answer.append(store[i])

        return (answer)




        