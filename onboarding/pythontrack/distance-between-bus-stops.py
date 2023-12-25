class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
       clock = sum(distance[min(start, destination): max(start, destination)])
       counter = sum(distance[:min(start, destination)]) + sum(distance[max(start,destination):])
       return min(clock, counter)
        
        