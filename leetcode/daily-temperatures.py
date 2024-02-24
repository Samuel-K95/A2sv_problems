class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                curr = stack.pop()
                ans[curr[1]] = i-curr[1]
            stack.append([temperatures[i], i])
        return ans

        