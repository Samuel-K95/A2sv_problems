# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        i = 0
        while i+1 < len(heights):
            if heights[i] >= heights[i+1]:
                i += 1
            else:
                need = heights[i] - heights[i+1]
                if bricks >= abs(need):
                    heappush(heap, need)
                    bricks -= abs(need)
                    i += 1
                else:
                    if ladders:
                        mx = 0
                        if heap:
                            if abs(heap[0]) > abs(need):
                                mx = heappop(heap)
                            else:
                                i += 1
                                ladders -= 1
                                continue
                        else:
                            ladders -= 1
                            i += 1
                            continue
                        bricks += abs(mx)
                        ladders -= 1
                    else:
                        return i

        return i
                    
