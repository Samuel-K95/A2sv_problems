# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for i in stones:
            heappush(max_heap, -i)

        while len(max_heap) > 1:
            large = heappop(max_heap)
            small = heappop(max_heap)

            if large != small:
                diff = abs(large - small)

                heappush(max_heap, -diff)
        
        if max_heap:
            return abs(max_heap.pop())

        return 0