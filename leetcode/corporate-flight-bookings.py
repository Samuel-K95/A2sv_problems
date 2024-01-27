class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        store = [0] * n
        for i in bookings:
            first = i[0] - 1
            store[first] += i[2]
            if i[1] < n:
                store[i[1]] -= i[2]
        for i in range(1, len(store)):
            store[i] += store[i-1]
        return store
        