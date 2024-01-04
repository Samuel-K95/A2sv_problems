class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        store = defaultdict(list)
        for i in range(len(costs)):
            store[costs[i]].append(costs[i])
        store = sorted(store.items(), key = lambda x: x[0])
        dup = []
        for i in store:
            dup.extend(i[1])
        c, amount = 0, 0
        for i in dup:
            if i + amount > coins:
                break
            amount += i
            c += 1
        return c

