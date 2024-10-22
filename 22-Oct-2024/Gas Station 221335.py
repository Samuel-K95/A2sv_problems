# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        store = 0
        ans = 0
        for i in range(len(gas)):
            store += (gas[i] - cost[i])

            if store < 0:
                store = 0
                ans = i + 1
        
        return ans if sum(gas) >= sum(cost) else -1
