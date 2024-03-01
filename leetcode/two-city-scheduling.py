class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: (x[0] - x[1]))
        stack = []
        n = len(costs)
        for i in range(n):
            app = 0
            if len(stack) >= n // 2:
                app = 1
            stack.append(costs[i][app])
        
        return sum(stack)