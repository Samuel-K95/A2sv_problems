class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        print(points)
        check=float('-inf')
        ans=0
        for i in range(0,len(points)):
            if check<points[i][0]:
                ans+=1
                check=points[i][1]

        return ans