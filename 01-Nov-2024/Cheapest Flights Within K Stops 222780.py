# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = []
        curr = [float('inf') for _ in range(n)]
        curr[src] = 0
        dp.append(curr)
        graph = defaultdict(list)
        pathes = defaultdict(int)

        for i in range(k+1):
            prev = dp[i-1][:]
            curr = dp[i-1]
            for u, v, w in flights:
                curr[v] = min(curr[v], prev[u] + w)
            dp.append(curr)
        
        ans = dp[-1][dst]
        return ans if ans != float('inf') else -1
            


        
