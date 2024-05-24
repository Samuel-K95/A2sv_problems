# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        mp = defaultdict(lambda:0)
        n = len(richer)

        indeg = [0 for _ in range(len(quiet))]
        for i in range(n):
            u, v = richer[i]
            graph[u].append(v)
            indeg[v] += 1

        for i in range(len(quiet)):
            mp[quiet[i]] = i


        ans = [quiet[i] for i in range(len(quiet))]

        queue = deque()
        vis = set()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)
                vis.add(i)

        while queue:
            front = queue.popleft()
            ans[front] = mp[quiet[front]]

            for neigh in graph[front]:
                indeg[neigh] -= 1
                quiet[neigh] = min(quiet[neigh], quiet[front])
                if indeg[neigh] == 0:
                    queue.append(neigh)
                    vis.add(neigh)

        return ans




        

        



