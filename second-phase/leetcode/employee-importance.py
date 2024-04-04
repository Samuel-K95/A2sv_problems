"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)

        for i in employees:
            graph[i.id].append((i.importance, i.subordinates))
        count = 0

        visisted = set()
        def dfs(node):
            nonlocal count
            if len(graph[node][0][1]) == 0:
                count += graph[node][0][0]
                return 

            visisted.add(node)
            count += graph[node][0][0]
            sub = graph[node][0][1]

            for i in sub:
                if i not in visisted:
                    dfs(i)

        dfs(id)

        return count
            
        
        
        