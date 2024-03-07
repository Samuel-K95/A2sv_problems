class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons

        self.times = times
        track = defaultdict(int)
        current_winner = self.persons[0]
        self.winners = [current_winner]
        track[current_winner] += 1

        for i in range(1, len(persons)):
            track[persons[i]] += 1
            if track[persons[i]] >= track[current_winner]:
                current_winner = persons[i]
            self.winners.append(current_winner)


    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)
        return self.winners[index-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)