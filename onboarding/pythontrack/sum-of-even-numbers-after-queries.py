class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = [i for i in nums if i % 2 == 0]
        evencheck = {i for i in range(len(nums)) if nums[i] % 2 == 0}
        dup = [j for j in nums]
        evensum = sum(evens)
        ans = []
        for i in range(len(nums)):
            index = queries[i][1]
            val = queries[i][0]
            nums[index] += val
            if nums[index] % 2 == 0:
                if index not in evencheck:
                    evencheck.add(index)
                    evensum += nums[index]
                else:
                    evensum += (nums[index] - dup[index])
            else:
                if index in evencheck:
                    evensum -= dup[index]
                    evencheck.discard(index)
            dup[index] = nums[index]
            ans.append(evensum)
        return ans

                
