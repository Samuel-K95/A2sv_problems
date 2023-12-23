class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = i
        for first, second in operations:
            ind = store[first]
            del store[first]
            store[second] = ind
        st = list((y, k) for k, y in store.items())
        st.sort(key=lambda v: v[0])
        ans = []
        for i in st:
            ans.append(i[1])
        return ans
