class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1][0] > val:
            self.minStack.append([val, 1])
        elif self.minStack and self.minStack[-1][0] == val:
            self.minStack[-1][1] += 1

    def pop(self) -> None:
        curr = self.stack.pop()
        if self.minStack and self.minStack[-1][0] == curr:
            self.minStack[-1][1] -= 1
        
        if self.minStack[-1][1] <= 0:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()