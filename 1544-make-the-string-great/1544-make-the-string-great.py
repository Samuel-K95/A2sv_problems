class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            curr = s[i].lower()
            if stack and stack[-1] == curr:
                if curr != s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                curr = s[i].upper()
                if stack and stack[-1] == curr:
                    if curr != s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])

        return "".join(stack)
