# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        gr = defaultdict(list)
        degree = [0  for _ in range(n)]
        for u, v in edges:
            gr[u].append(v)
            gr[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        store = deque()
        vis = set()
        for i in range(n):
            if degree[i] == 1:
                store.append(i)
                vis.add(i)
        
        ans = []
        while n > 2:
            bound = len(store)
            n -= bound

            for _ in range(bound):
                front = store.popleft()
                for child in gr[front]:
                    if child not in vis:
                        degree[child] -= 1
                        if degree[child] == 1:
                            store.append(child)
                            vis.add(child)

        return list(store) if store else [0]



