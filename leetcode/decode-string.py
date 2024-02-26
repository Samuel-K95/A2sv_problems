class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # s = s.partition(']')
        # print(s)
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            elif s[i] == ']':
                tempstack = []
                while stack and stack[-1] != '[':
                    temp = stack.pop()
                    tempstack.append(temp)
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    n = stack.pop()
                    num.append(n)
                if len(num) > 0:
                    num.reverse()
                    num = int("".join(num))
                    tempstack = num * tempstack
                    tempstack.reverse()
                    stack.extend(tempstack)


        return "".join(stack)

                