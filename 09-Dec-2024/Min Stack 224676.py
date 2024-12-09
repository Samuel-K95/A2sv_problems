# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.track = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        prev = float('inf')
        if self.track:
            prev = self.track[-1]
        
        if val <= prev:
            self.track.append(val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        if self.track[-1] == top:
            self.track.pop()
        return top
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.track[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()