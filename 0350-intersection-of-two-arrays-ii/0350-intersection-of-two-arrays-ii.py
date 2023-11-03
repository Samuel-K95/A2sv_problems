class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        store_1 = Counter(nums1)
        store_2 = Counter(nums2)
        store = {}
        small = nums1 if len(nums1) <= len(nums2) else nums2
        large = nums1 if len(nums1) > len(nums2) else nums2
        for i, val in enumerate(large):
            if store_1[val] and store_2[val]:
                key = val
                value = store_1[val] if store_1[val] <= store_2[val] else store_2[val]
                store[key] = value
        for i in small:
            if i in store:
                ans.append(i)
                store[i] -= 1
                if store[i] == 0:
                    del store[i]
        ans.sort()
        return ans