# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        for i in range(1, len(height)):
            curr = height[i]
            prev = max(left[-1], height[i-1])
            if curr < prev:
                left.append(prev)
            else:
                left.append(0)
        
        right = [0]

        for i in range(len(height)-2, -1, -1):
            curr = height[i]
            nxt = max(right[-1], height[i+1])
            if curr < nxt:
                right.append(nxt)
            else:
                right.append(0)
        
        ans = 0

        right.reverse()
        for i in range(len(height)):
            if left[i] and right[i]:
                mn = min(left[i], right[i])
                ans += (mn - height[i])

        return ans