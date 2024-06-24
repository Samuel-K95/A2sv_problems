# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        fir, sec = 0, 0
        while fir < m and sec < n:
            if nums1[fir] > nums2[sec]:
                nums1[fir], nums2[sec] = nums2[sec], nums1[fir]
                for s in range(n-1):
                    if nums2[s] > nums2[s+1]:
                        nums2[s], nums2[s+1] = nums2[s+1], nums2[s]
            fir += 1
        
        while fir < len(nums1) and sec < len(nums2):
            nums1[fir] = nums2[sec]
            fir += 1
            sec += 1
        
            
