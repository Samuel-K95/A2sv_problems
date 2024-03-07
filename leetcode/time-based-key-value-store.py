class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.time[key]
        temp  =[]
        while store and store[-1][1] > timestamp:
            curr = store.pop()
            temp.append(curr)
        store.append([value, timestamp])
        if temp:
            temp.reverse()
            store.extend(temp)
        self.time[key] = store

    def get(self, key: str, timestamp: int) -> str:
        store = self.time[key]
        left = 0
        right = len(store) - 1
        # print(store)
        while left <= right:
            mid = left + (right - left) // 2

            if store[mid][1] == timestamp:
                return store[mid][0]
            
            if store[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if not store or store and store[right][1] > timestamp :
            return ""
        return store[right][0]
    
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)