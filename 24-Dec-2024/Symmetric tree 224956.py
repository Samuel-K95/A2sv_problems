# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSym(left, right):
            if not left and not right:
                return True
            
            if left and not right:
                return False
            
            if right and not left:
                return False
            
            if left.val != right.val:
                return False
            
            return checkSym(left.left, right.right) and checkSym(left.right, right.left)
        
        return checkSym(root, root)