class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        ret = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(str(n) for n in ret)))
