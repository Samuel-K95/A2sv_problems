# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSame(node1, node2):
            if not node1 and not node2:
                return True    
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
                
            if node1.val != node2.val:
                return False
            return isSame(node1.right,node2.right) and isSame(node1.left, node2.left)
        
        return isSame(p, q)