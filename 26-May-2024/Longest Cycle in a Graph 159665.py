# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        n = len(edges)

        indeg = [0 for _ in range(n)]
        outdeg = [0 for _ in range(n)]

        for i in range(n):
            if edges[i] == -1:
                continue
            graph[i].append(edges[i])
            indeg[edges[i]] += 1
            outdeg[i] += 1
        
        vis = set()
        vis = set()
        color = [0 for _ in range(n)]
        def dfs(node, depth):
            color[node] = 1
            ans  = 0
            for neigh in graph[node]:
                if color[neigh] == 0:
                    vis.add(neigh)
                    ans = ans + dfs(neigh, depth+1)
                elif color[neigh] == 1:
                    return depth + 1

            color[node] = 2

            return ans
        queue = deque()
        check = set()
        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)
                check.add(i)
                
        while queue:
            front = queue.popleft()

            for neigh in graph[front]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    queue.append(neigh)
                    check.add(neigh)
                
        def count_cycle(i):
            if indeg[i] == 0 or outdeg[i] == 0:
                return 0
            curr = 0
            if i not in vis:
                vis.add(i)
                curr = dfs(i, 0)

            return curr

        ans = 0
        for i in range(n):
            ans = max(ans, count_cycle(i))
        
        return ans if ans != 0 else -1

            

            

    



        

        
