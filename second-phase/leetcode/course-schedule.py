class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 0
        GREY = 1
        BLACK = 2   

        graph = defaultdict(list)
        state = defaultdict(int)
        possible = True
        for u, v in prerequisites:
            graph[u].append(v)
            state[v] = WHITE
            state[u] = WHITE
        
        def dfs(node):
            nonlocal possible
            if state[node] == GREY:
                possible = False
                return
            
            state[node] = GREY

            for i in graph[node]:
                if state[i] == WHITE:
                    dfs(i)
                elif state[i] == GREY:
                    possible = False
                    return
                
            state[node] = BLACK

        for u, v in prerequisites:
            if state[u] == WHITE:
                dfs(u)
        return possible
        