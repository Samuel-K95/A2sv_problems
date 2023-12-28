class RandomizedSet:

    def __init__(self):
        self.random = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.discard(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(sorted(self.random), 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()