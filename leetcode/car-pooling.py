class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        size = trips[0][2]
        store = [0] * size
        ded = defaultdict(int)
        for i in range(len(trips)):
            if trips[i][2] > len(store) or trips[i][1] > len(store):
                store.extend([0] * (trips[i][2] - len(store)))
            store[trips[i][1]] += trips[i][0]
            ded[trips[i][2] - 1] += trips[i][0]
        pref = 0
        for i in range(len(store)):
            pref += store[i]
            if pref > capacity:
                return False
            if i in ded:
                pref -= ded[i]
            if pref > capacity:
                return False
        return True
