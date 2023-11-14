class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = 0
        t = 0
        match = 0
        players.sort()
        trainers.sort()
        while True:
            if t >= len(trainers) or p >= len(players):
                break
            while t < len(trainers) and p < len(players) and players[p] > trainers[t]:
                t += 1
            if t < len(trainers) and players[p] <= trainers[t]:
                match += 1
                t += 1
                p += 1
        return match
