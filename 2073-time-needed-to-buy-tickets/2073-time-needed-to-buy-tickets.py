class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        rem = set()
        while True:
            i = i % len(tickets)
            if i not in rem:
                tickets[i] -= 1
                count += 1
                if tickets[i] == 0 and i == k:
                    return count
                elif tickets[i] == 0:
                    rem.add(i)
            i += 1

