class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        tot = capacity
        step = 0
        for i in range(len(plants)):
            if plants[i] <= capacity:
                capacity -= plants[i]
                step += 1
                if i + 1 < len(plants) and plants[i+1] > capacity:
                    step += (i + 1) * 2
                    capacity = tot
            else:
                step += (i + 1)
                step += (i + 1)
                capacity = tot - plants[i]




        return step