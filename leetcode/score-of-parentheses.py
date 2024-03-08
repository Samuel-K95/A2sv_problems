class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += (top * 2)
        return stack[-1]
        

