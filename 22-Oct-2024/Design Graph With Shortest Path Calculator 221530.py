# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for u, v, w in edges:
            self.graph[u].append((v, w))
        self.n = n
        

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w)) 
        

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf') for _ in range(self.n)]
        queue = deque()
        in_queue = set()
        queue.append(node1)
        in_queue.add(node1)
        distances[node1] = 0

        while queue:
            node = queue.popleft()
            in_queue.remove(node)

            for v, w in self.graph[node]:
                if distances[node] != float('inf'):
                    new_dist = distances[node] + w
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        if v not in in_queue:
                            in_queue.add(v)
                            queue.append(v)

        return distances[node2] if distances[node2] != float('inf') else -1

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)