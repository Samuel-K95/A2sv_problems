class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0
        ans = float('inf')
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                ans = min(ans, nums1[first])
                first += 1
                second += 1
            else:
                if nums1[first] < nums2[second]:
                    while first < len(nums1) and nums1[first] < nums2[second]:
                        first += 1
                elif nums2[second] < nums1[first]:
                    while second < len(nums2) and nums2[second] < nums1[first]:
                        second += 1
        return ans if ans != float('inf') else -1