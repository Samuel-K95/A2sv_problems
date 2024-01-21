class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = [nums[0]]
        for i in range(1, len(nums)):
            self.pref.append(self.pref[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        right = self.pref[right]
        left = self.pref[left - 1] if left > 0 else 0
        return right - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)