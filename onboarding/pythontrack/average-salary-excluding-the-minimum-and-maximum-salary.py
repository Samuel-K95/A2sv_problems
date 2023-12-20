class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum_ = 0
        c = 0
        for i in range(1, len(salary) - 1):
            sum_ += salary[i]
            c += 1
        print(sum_, c)
        return sum_ / c