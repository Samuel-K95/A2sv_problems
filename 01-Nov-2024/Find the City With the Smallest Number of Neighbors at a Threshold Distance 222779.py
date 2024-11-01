# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        a = [[float('inf') for _ in range(n)] for _ in range(n)]
        costs = defaultdict(int)

        for u, v , w in edges:
            costs[(u, v)] = w
            costs[(v, u)] = w

        for r in range(n):
            for c in range(n):
                if r == c:
                    a[r][c] = 0
                elif (r, c) in costs:
                    a[r][c] = costs[(r, c)]
                    a[c][r] = costs[(r, c)]
        
        for i in range(n):
            for r in range(n):
                for c in range(n):
                    if r == i or c == i:
                        continue
                    a[r][c] = min(a[r][c], a[r][i] + a[i][c])
                    a[c][r] = a[r][c]

        mx = float(inf)
        city = 0
        for r in range(n):
            curr = 0
            for c in range(n):
                if a[r][c] <= distanceThreshold:
                    curr += 1
            if curr <= mx:
                mx = curr
                city = r
                
        return city


        
