class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        store = deque()
        for i in range(len(tickets)):
            store.append([tickets[i], i])
        op = 0
        while store:
            curr = store.popleft()
            curr[0] -= 1
            op += 1
            if curr[0] > 0:
                store.append(curr)
            elif curr[1] == k:
                break
        return op


                

