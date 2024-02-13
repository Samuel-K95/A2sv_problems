class Solution:
    def bestClosingTime(self, customers: str) -> int:
        opened = [0] * len(customers)
        closed = [1] * len(customers)
        for i in range(len(customers)):
            if customers[i] == 'Y':
                opened[i] = 1
                closed[i] = 0
            if i > 0:
                opened[i] += opened[i-1]
                closed[i] += closed[i-1]
        tot = opened[-1]
        store = defaultdict(int)
        for i in range(len(opened)):
            lef = 0
            lefy = 0
            if i > 0 :
                lef = opened[i-1]
                lefy = closed[i-1]
            store[i] = (tot-lef) + lefy
        store[i+1] = closed[-1]
        targ = min(store.values())
        for i in store:
            if store[i] == targ:
                return i
            
