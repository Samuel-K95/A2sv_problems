class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '/', '-', '*'}
        for i in range(len(tokens)):
            if tokens[i] in ops:
                b = stack.pop()
                a = stack.pop()
                c = str(int(eval(a + tokens[i] + b)))
                stack.append(c)
            else:
                stack.append(tokens[i])

        return int(stack[0])
