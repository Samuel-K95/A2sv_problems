# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indeg = [0 for _ in range(numCourses)]

        graph = defaultdict(list)
        collect = defaultdict(set)

        for u, v in prerequisites:
            indeg[v] += 1
            graph[u].append(v)
        
        queue = deque()
        vis = set()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)
                vis.add(i)
        

        while queue:
            front = queue.popleft()

            for neigh in graph[front]:
                indeg[neigh] -= 1
                for v in collect[front]:
                    collect[neigh].add(v)
                collect[neigh].add(front)

                if indeg[neigh] == 0 and neigh not in vis:
                    queue.append(neigh)
                    vis.add(neigh)

        ans = []
        for u, v in queries:
            if u in collect[v]:
                ans.append(True)
            else:
                ans.append(False)

        
        return ans 
        
