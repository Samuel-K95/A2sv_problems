class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        min_que = deque()
        max_que = deque()
        ans = 0
        for end in range(len(nums)):
            curr = nums[end]
            if not min_que:
                min_que.append(nums[end])
            else:
                while min_que and min_que[-1] < curr:
                    min_que.pop()
                min_que.append(curr)
            if not max_que:
                max_que.append(nums[end])
            else:
                while max_que and max_que[-1] > curr:
                    max_que.pop()
                max_que.append(nums[end])
            while start < len(nums) and min_que and max_que and  abs(min_que[0] - max_que[0] ) > limit:
                left = nums[start]
                if left == min_que[0]:
                    min_que.popleft()
                if left == max_que[0]:
                    max_que.popleft()
                start += 1
            ans = max(ans, end - start + 1)
        return ans
            