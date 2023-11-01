class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        large=m+n
        if large!=len(nums1):
            for i in range(n):
                nums1.append(0)
        for i in range(n):
            nums1[large-n+i]=nums2[i]

        nums1.sort()
        print(nums1)
    