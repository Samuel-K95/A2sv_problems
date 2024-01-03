class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_area = 0
        points.sort()
        for i in range(len(points) - 1):
            max_area = max(points[i+1][0] - points[i][0], max_area)
        return max_area