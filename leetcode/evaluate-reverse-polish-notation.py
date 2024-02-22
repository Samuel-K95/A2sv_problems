class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(a, b , op):
            if op == '+':
                return str(int(int(a) + int(b)))
            elif op == '-':
                return str(int(int(a) - int(b)))
            elif op == '*':
                return str(int(int(a) * int(b)))
            elif op == '/':
                return str(int(int(a) / int(b)))

        stack = []
        ops = {'+', '/', '-', '*'}
        for i in range(len(tokens)):
            if tokens[i] in ops:
                b = stack.pop()
                a = stack.pop()
                c = calc(a, b, tokens[i])
                stack.append(c)
            else:
                stack.append(tokens[i])

        return int(stack[0])
