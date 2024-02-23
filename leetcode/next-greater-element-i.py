class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = Counter(nums1)
        ans = defaultdict(int)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                if stack[-1] in check:
                    ans[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        fin = [-1] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] in ans:
                fin[i] = ans[nums1[i]]
        return fin

        

