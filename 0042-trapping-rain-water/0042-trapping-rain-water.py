class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        tot = 0
        left_max , right_max = height[left], height[right]
        while left < right:
            if left_max <= right_max:
                tot += (left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])
            else:
                tot += (right_max-height[right])
                right -= 1
                right_max = max(right_max, height[right])
        return tot