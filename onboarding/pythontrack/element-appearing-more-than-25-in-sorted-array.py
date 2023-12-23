class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0.25 * len(arr)
        store = Counter(arr)
        for i in store:
            if store[i] > count:
                return i


            
