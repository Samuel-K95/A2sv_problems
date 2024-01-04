class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = defaultdict(list)
        for i in range(len(points)):
            dist = sqrt(pow(points[i][0], 2)  + pow(points[i][1], 2))
            store[dist].append(points[i])
        ans = sorted(store.items(), key = lambda x: x[0])
        fin = []
        for i in ans:
            fin.extend(i[1])
        return fin[:k]