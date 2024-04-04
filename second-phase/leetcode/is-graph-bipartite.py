class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        check = [-1 for _ in range(len(graph))]
        
        def dfs(node, k):
            check[node] = k
            temp=True
            for i in graph[node]:
                if check[i] == -1:
                    temp=temp and dfs(i, 1-k)
                else:
                    if check[i] == check[node]:
                        return False
            return temp
        
        for i in range(len(graph)):
            if check[i] == -1:
                if not dfs(i, 1):
                    return False
        return True

