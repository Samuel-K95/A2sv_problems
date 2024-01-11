class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        store = defaultdict(int)
        for curr in range(len(nums)):
            left = curr + 1
            right = len(nums) - 1
            pick, curr_coll = float('inf'), tuple()
            while left < right:
                current_sum = nums[curr] + nums[left] + nums[right]
                if abs(target-current_sum) < pick:
                    pick = abs(target-current_sum)
                    curr_coll = (nums[curr], nums[left], nums[right])
                if nums[curr] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            store[curr_coll] = pick
        store = sorted(store.items(), key = lambda x: x[1])
        return sum(store[0][0])


