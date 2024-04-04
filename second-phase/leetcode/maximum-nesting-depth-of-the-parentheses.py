class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                ans = max(ans, len(stack))
                stack.pop()
        return ans
