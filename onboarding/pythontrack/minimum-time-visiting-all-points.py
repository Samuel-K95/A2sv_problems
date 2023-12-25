class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points)-1):
            xdiff = points[i+1][0] - points[i][0]
            ydiff = points[i+1][1] - points[i][1]
            # print(xdiff, ydiff)
            steps += max(abs(xdiff), abs(ydiff))
        return steps


        