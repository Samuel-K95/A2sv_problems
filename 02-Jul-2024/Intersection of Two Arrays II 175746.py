# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        fin = []
        second_store = Counter(nums2)

        first_store = Counter(nums1)
        store = {}


        little = nums1 if len(nums1) <= len(nums2) else nums2
        large = nums1 if len(nums1) > len(nums2) else nums2
        for i, val in enumerate(large):
            if first_store[val] and second_store[val]:
                key = val
                value = first_store[val] if first_store[val] <= second_store[val] else second_store[val]
                store[key] = value

        for i in little:
            if i in store:
                fin.append(i)
                store[i] -= 1
                if store[i] == 0:
                    del store[i]
        fin.sort()
        return fin