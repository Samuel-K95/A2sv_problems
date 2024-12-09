# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = defaultdict(list)
        nums = list(set(nums))

        for i in range(len(nums)):
            left, right = [], []

            if nums[i]-1 in store:
                left = store[nums[i]-1]
            
            if nums[i]+1 in store:
                right = store[nums[i]+1]
            
            if left and right:
                lpt = left[0]
                rpt = right[0]
                left_list = store[lpt]
                right_list = store[rpt]

                if left_list[1] > right_list[1]:
                    left_list[1] += right_list[1]
                    left_list[1] += 1
                    store[nums[i]] = left_list
                    store[nums[i]-1] = left_list
                    store[nums[i] + 1] = left_list
                    store[rpt] = left_list
                    store[lpt] = left_list
                else:
                    right_list[1] += left_list[1]
                    right_list[1] += 1
                    store[nums[i]] = right_list
                    store[nums[i]-1] = right_list
                    store[nums[i]+1] = right_list
                    store[rpt] = right_list
                    store[lpt] = right_list
            elif left:
                lpt = left[0]
                left_list = store[lpt]
                left_list[1] += 1
                store[nums[i]] = left_list
                store[lpt] = left_list
            elif right:
                rpt = right[0]
                right_list = store[rpt]
                right_list[1] += 1
                store[nums[i]] = right_list
                store[rpt] = right_list
            else:
                store[nums[i]] = [nums[i], 1]
        
        ans = 0
        for key in store:
            ans = max(ans, store[key][1])

        return ans