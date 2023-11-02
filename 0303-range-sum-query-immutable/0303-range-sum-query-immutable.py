class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0
        for i in nums:
            total += i
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preleft = self.prefix[left - 1] if left > 0 else 0
        preright = self.prefix[right]
        return preright - preleft

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)