class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            left = stack[-1]
            right = star[-1]
            if left < right:
                stack.pop()
                star.pop()
            else:
                break
        if stack:
            return False
        return True
