class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(i-x) for i in arr]
        store = defaultdict(list)

        for i in range(len(diff)):
            store[diff[i]].append(arr[i])
            
        ref = []
        for i in range(max(diff) + 1):
            ref.extend(store[i])

        if  k < len(ref):
            ans = ref[:k]
        else:
            ans = ref

        return sorted(ans)
        
