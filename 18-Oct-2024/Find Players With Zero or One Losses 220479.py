# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        loosers = defaultdict(int)

        for w, l in matches:
            winners[w] += 1
            loosers[l] += 1
        
        winner , loser = [], []

        for val in winners:
            if val not in loosers:
                winner.append(val)
        
        for val in loosers:
            if loosers[val] == 1:
                loser.append(val)
            
        winner.sort()
        loser.sort()

        return [winner, loser]