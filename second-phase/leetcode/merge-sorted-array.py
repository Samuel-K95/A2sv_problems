class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first , second = 0, 0
        while first < m and second < n:
            if nums1[first] <= nums2[second]:
                first += 1
            else:
                nums1[first], nums2[second] = nums2[second], nums1[first]
                curr = second
                while curr + 1 < n and nums2[curr+1] < nums2[curr]:
                    nums2[curr+1], nums2[curr] = nums2[curr], nums2[curr+1]
                    curr += 1
        nums1[m:] = nums2[:]
        
        