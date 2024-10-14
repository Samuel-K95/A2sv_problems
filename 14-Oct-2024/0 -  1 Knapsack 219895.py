# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        
        def dp(idx, cap):
            if idx == len(val):
                return 0
            
            
            take = 0
            if wt[idx] <= cap:
                take = val[idx] + dp(idx + 1, cap - wt[idx])
            
            not_take = dp(idx + 1, cap)
            
            return max(take, not_take)
        
        return dp(0, W)