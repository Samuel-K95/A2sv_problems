# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maximum = 0
        points.sort()

        
        for i in range(len(points) - 1):
            maximum = max(points[i+1][0] - points[i][0], maximum)
        return maximum