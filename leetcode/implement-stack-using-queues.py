class MyStack:

    def __init__(self):
        self.stack = []
        self.curr = -1

    def push(self, x: int) -> None:
        curr = self.curr + 1
        if curr > len(self.stack) - 1:
            self.stack.append(x)
        else:
            self.stack[curr] = x
        self.curr = curr
        

    def pop(self) -> int:
        val = self.stack[self.curr]
        self.curr -= 1
        return val
        

    def top(self) -> int:
        val = self.stack[self.curr]
        return val

    def empty(self) -> bool:
        if self.curr == -1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()