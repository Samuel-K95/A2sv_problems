class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = [i for i in nums if i < pivot]
        larger = [i for i in nums if i > pivot]
        equal = [ i for i in nums if i == pivot]
        sm = 0
        s = len(smaller)
        e = len(equal)
        l = len(larger)
        for i in range(len(smaller)):
            nums[i] = smaller[i]
        sm += s
        for j in range(len(equal)):
            nums[sm + j] = equal[j]
        sm += e
        for k in range(len(larger)):
            nums[sm + k] = larger[k]
        return nums