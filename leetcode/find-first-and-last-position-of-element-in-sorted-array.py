class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        fir = float('inf')
        sec = float('-inf')

        sec_left = 0 
        sec_right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                fir = min(mid, fir)
                right = mid - 1
            
        while sec_left <= sec_right:
            mid = sec_left + (sec_right - sec_left) // 2

            if nums[mid] < target:
                sec_left = mid + 1
            elif nums[mid] > target:
                sec_right = mid - 1
            else:
                sec = max(sec, mid)
                sec_left = mid + 1

        return [fir, sec] if fir != float('inf') and sec != float('-inf') else [-1, -1]
            
            
            
