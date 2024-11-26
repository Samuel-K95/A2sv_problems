# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.store = defaultdict(list)
        self.start = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, st_time = self.start[id]
        self.store[(station, stationName)].append(t-st_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        lst = self.store[(startStation, endStation)]
        return sum(lst) / len(lst)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)