class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        store = defaultdict(int)
        ranges.sort()
        for i in range(len(ranges)):
            count = ranges[i][0]
            while count <= ranges[i][1]:
                store[count] += 1
                count += 1
        j = left
        print(left, store)
        while j <= right:
            if store[j] == 0:
                return False
            j += 1
        return True