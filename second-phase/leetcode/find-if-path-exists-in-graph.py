class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        visited = set()
        def find(n):
            if n == destination:
                return True

            visited.add(n)

            for j in graph[n]:
                if j not in visited:
                    found = find(j)
                    if found:
                        return True
            return False
        return find(source)