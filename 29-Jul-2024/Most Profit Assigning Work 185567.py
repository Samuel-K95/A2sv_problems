# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mx = float('-inf')
        n = len(difficulty)

        mp =[[difficulty[i], profit[i]] for i in range(n)]

        mp.sort()
        difficulty.sort()

        for i in range(n):
            diff, prof = mp[i]
            mx = max(mx, prof)
            mp[i][1] = mx
        
        ans = 0
        for w in worker:
            idx = bisect_right(difficulty, w)

            if idx < n and mp[idx][0] <= w:
                ans += mp[idx][1]
            elif idx > 0 and mp[idx-1][0] <= w:
                ans += mp[idx-1][1]
        
        return ans


        





        