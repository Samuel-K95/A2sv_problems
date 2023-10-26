class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> List[int]:
        store = {}
        dup = []
        for i in range(len(nums)):
            dup.append(nums[i])
        nums.sort()
        answer = []
        for i in range(len(nums)):
            try:
                store.setdefault(nums[i], i)
            except:
                continue

        for i in dup:
            answer.append(store[i])

        return answer
