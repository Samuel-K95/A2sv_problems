class ATM:

    def __init__(self):
        self.bank = [20, 50, 100, 200, 500]
        self.count = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.count[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        ret = [0] * 5

        for i in range(len(self.bank) - 1, -1, -1):
            use = min(amount // self.bank[i], self.count[i])
            ret[i] = use
            amount -= use * self.bank[i]
        if amount != 0:
            return [-1]
        
        for i in range(len(ret)):
            self.count[i] -= ret[i]
        
        return ret


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)