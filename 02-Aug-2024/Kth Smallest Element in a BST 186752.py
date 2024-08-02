# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            store.append(node.val)
            traverse(node.right)
            
        traverse(root)
        
        return store[k-1]

            
            


        