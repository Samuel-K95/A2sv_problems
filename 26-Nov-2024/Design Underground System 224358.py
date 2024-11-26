# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.store = defaultdict(list)
        self.start = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, st_time = self.start[id]
        diff = t-st_time
        if (station, stationName) in self.store:
            self.store[(station, stationName)][0] += diff
            self.store[(station, stationName)][1] += 1
        else:
            self.store[(station, stationName)] = [diff, 1]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.store[(startStation, endStation)][0] / self.store[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)