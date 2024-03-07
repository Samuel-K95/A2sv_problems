class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index = defaultdict(int)
        ref = []

        for i in range(len(intervals)):
            index[intervals[i][0]] = i
            ref.append(intervals[i][0])
        
        ref.sort()
        ans = [-1] * len(intervals)
        
        for i in range(len(intervals)):
            j = intervals[i][1]
            ind = bisect_left(ref, j)
            if ind < len(ans):
                ans[i] = index[ref[ind]]

        return ans