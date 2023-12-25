class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loser = defaultdict(int)
        for i in range(len(matches)):
            winner[matches[i][0]] += 1
            loser[matches[i][1]] += 1
        win = []
        los = []
        for i in winner:
            if i not in loser:
                win.append(i)
        for j in loser:
            if loser[j] == 1:
                los.append(j)
        win.sort()
        los.sort()
        return [win, los]
        