class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        proc = defaultdict(lambda: float('-inf'))
        j = 0
        for i in range(1, len(tasks)):
            proc[processorTime[j]] = max(processorTime[j]+tasks[i-1], proc[processorTime[j]])
            if i % 4 == 0:
                j += 1
        return max(proc.values())


        