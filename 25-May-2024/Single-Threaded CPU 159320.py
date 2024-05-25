# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        ans = []
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        tasks.sort()

        processing = tasks[0][0]
        i = 0
        while i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= processing:
                heappush(available, [tasks[i][1], tasks[i][2]])
                i += 1

            if available:
                front, idx = heappop(available)
                ans.append(idx)
                processing += front
            else:
                processing = tasks[i][0]

        while available:
            front, idx = heappop(available)
            ans.append(idx)

        return ans




