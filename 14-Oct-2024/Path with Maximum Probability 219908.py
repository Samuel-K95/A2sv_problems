# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distances = {i:0 for i in range(n)}

        heap = [(-1, start_node)]

        graph = defaultdict(list)
        processed = set()
        pathes = defaultdict(int)


        for i in range(len(succProb)):
            u, v = edges[i]
            graph[u].append(v)
            graph[v].append(u)
            pathes[(u, v)] = succProb[i]
            pathes[(v, u)] = succProb[i] 


        
        while heap:
            dist, node = heappop(heap)

            if node in processed:
                continue
            
            processed.add(node)
            for child in graph[node]:
                d = max(distances[child], pathes[(node, child)] * (-1 * dist))
                if d > distances[child]:
                    distances[child] = d
                    heappush(heap, (-d, child))
        ans = distances[end_node]

        return  ans if ans != float('-inf') else 0
            
        
