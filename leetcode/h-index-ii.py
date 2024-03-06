class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = citations[-1]
        ans = left

        while left <= right:
            mid = left + (right - left) // 2

            c = 0
            for i in range(len(citations)):
                if citations[i] >= mid:
                    c += 1

            if c < mid:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
            
        return ans


        