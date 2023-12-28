class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(list)
        self.time = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.checkin[id][0]
        initial = self.checkin[id][1]

        self.time[(start, stationName)].append(abs(initial - t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        store = []
        for i in self.time:
            if i == (startStation,endStation):
                return sum(self.time[i]) / len(self.time[i])

        

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)