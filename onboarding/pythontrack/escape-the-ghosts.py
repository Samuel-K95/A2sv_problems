class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        startx, starty = 0, 0
        myturn = 0
        if startx != target[0]:
            myturn += (startx - target[0]) if startx > target[0] else (target[0] - startx)
        if starty != target[1]:
            myturn += (starty - target[1]) if starty > target[1] else (target[1] - starty)
        ghoststeps = defaultdict(int)
        for i in range(len(ghosts)):
            turn = 0
            if ghosts[i][0] != target[0]:
                turn += (ghosts[i][0] - target[0]) if ghosts[i][0] > target[0] else (target[0] - ghosts[i][0])
            if ghosts[i][1] != target[1]:
                turn += (ghosts[i][1] - target[1]) if ghosts[i][1] > target[1] else (target[1] - ghosts[i][1])
            ghoststeps[i] = turn
        print(ghoststeps, myturn)
        for i in ghoststeps:
            if ghoststeps[i] <= myturn:
                return False
        
        return True



        