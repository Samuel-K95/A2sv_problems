class Bitset:
    def __init__(self, size: int):
        self.bitset = ['0'] * size
        self.inverted = ['1'] * size
        self.check = Counter(self.bitset)
        

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == '0':
            self.bitset[idx] = '1'
            self.inverted[idx] = '0'
            self.check['1'] += 1
            self.check['0'] -= 1



    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == '1':
            self.bitset[idx] = '0'
            self.check['1'] -= 1
            self.check['0'] += 1
            self.inverted[idx] = '1'

    def flip(self) -> None:
        self.bitset, self.inverted = self.inverted, self.bitset
        self.check['1'], self.check['0'] = self.check['0'], self.check['1']

    def all(self) -> bool:
        if self.check['1'] == len(self.bitset):
            return True
        return False
        

    def one(self) -> bool:
        if self.check['1'] > 0:
            return True
        return False

    def count(self) -> int:
        if '1' in self.check:
            return self.check['1']
        return 0

    def toString(self) -> str:
        return "".join(self.bitset)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()