class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = defaultdict(int)
        for i in range(len(arr2)):
            order[arr2[i]] = i
        store = defaultdict(list)
        for i in range(len(arr1)):
            if arr1[i] in order:
                store[order[arr1[i]]].append(arr1[i])
            else:
                store[-1].append(arr1[i])
        ans = []
        for i in arr2:
            ans.extend(store[order[i]])
        store[-1].sort()
        ans.extend(store[-1])
        return ans

        