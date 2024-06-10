# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mx = max(days)
        dp = defaultdict(lambda:0)

        traveldays = set(days)

        for i in range(1, mx+1):
            if i not in traveldays:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
            
        return max(dp[mx], dp[mx-1])
