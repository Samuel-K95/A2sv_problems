class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = set()
        to_be_count = nums1 if len(nums1) < len(nums2) else nums2
        to_iterate = nums1 if len(nums1) > len(nums2) else nums2
        store = Counter(to_be_count)
        for i, val in enumerate(to_iterate):
            if val not in ans and store[val]:
                ans.add(val)
        return list(ans)