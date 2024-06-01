# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def traverse(node):
            if not node:
                return 0
            
            mx = 0
            if node:
                for child in node.children:
                    mx = max(mx, traverse(child))

            return 1 + mx
        

        return traverse(root)