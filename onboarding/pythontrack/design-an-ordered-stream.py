class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.store = defaultdict(int)
        self.check = [0] * n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey - 1] = value
        self.check[idKey - 1] = 1
        ptr = self.ptr
        ans = []
        while ptr < len(self.check) and self.check[ptr] == 1:
            ans.append(self.store[ptr])
            ptr += 1
        self.ptr = ptr
        return ans

        
        

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)