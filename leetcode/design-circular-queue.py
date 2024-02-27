class MyCircularQueue:

    def __init__(self, k: int):
        self.circular = deque()
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.circular) < self.size:
            self.circular.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.circular) > 0:
            self.circular.popleft()
            return True
        return False

    def Front(self) -> int:
        if len(self.circular) > 0:
            return self.circular[0]
        return -1

    def Rear(self) -> int:
        if len(self.circular) > 0:
            return self.circular[-1]
        return -1


    def isEmpty(self) -> bool:
        if len(self.circular) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.circular) == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()