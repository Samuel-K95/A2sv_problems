# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    free = [1 for _ in range(V)]
	    
	    for i in range(V):
	        if free[i]:
	            free[i] = 0
	            stack = [i]
        	    while stack:
        	        node = stack.pop()
        	        count = 0
        	        for neigh in adj[node]:
        	            if free[neigh]:
        	                free[neigh] = 0
        	                stack.append(neigh)
        	            else:
        	                count += 1
        	        if count > 1:
        	            return True
	    return False