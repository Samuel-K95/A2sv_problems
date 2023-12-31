class FrequencyTracker:

    def __init__(self):
        self.number = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        before = self.number[number]
        self.number[number] += 1
        self.freq[before] -= 1
        self.freq[1 + before] +=  1

    def deleteOne(self, number: int) -> None:
        before = self.number[number]
        if before == 0:
            return 
        
        self.number[number] -= 1
        self.freq[before] -= 1
        self.freq[before - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] >= 1



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)