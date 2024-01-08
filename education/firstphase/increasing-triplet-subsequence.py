class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # store = defaultdict(int)
        store = []
        for i in range(len(nums)):
            place = bisect_left(store, nums[i])

            if place < len(store):
                store[place] = nums[i]
            else:
                store.append(nums[i])
            if len(store)>2:
                return True

            
        return False
        
