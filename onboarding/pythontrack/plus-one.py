class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = [str(i) for i in digits]
        num = int("".join(num)) + 1
        nums = [int(i) for i in str(num)]
        return nums