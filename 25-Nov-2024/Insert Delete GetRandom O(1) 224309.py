# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.mp = defaultdict(int)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.mp[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mp:
            idx = self.mp[val]
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            self.arr.pop()
            if idx < len(self.arr):
                vl = self.arr[idx]
                self.mp[vl] = idx
            
            del self.mp[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()