class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: (x[0] - x[1]))
        stack = 0
        n = len(costs)
        for i in range(n):
            app = 0
            if i >= n // 2:
                app = 1
            stack  += costs[i][app]
        
        return stack