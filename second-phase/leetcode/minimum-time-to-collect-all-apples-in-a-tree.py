class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        vis = set()
        def dfs(node):
            if len(graph[node]) == 0:
                return 2 if hasApple[node] and node != 0 else 0
            
            curr = 0
            vis.add(node)
            for i in graph[node]:
                if i not in vis:
                    curr += dfs(i)
            
            if curr == 0:
                if hasApple[node] and node != 0:
                    return 2
                else:
                    return 0
            else:
                if node == 0:
                    return curr
                else:
                    return curr + 2

        ans = dfs(0)
        return ans
            