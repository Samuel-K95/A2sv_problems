# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        stack = []

        def traverse(node, low, high):
            if not node:
                return
            
            if low <= node.val and node.val <= high:
                stack.append(node.val)
                traverse(node.left, low, high)
                traverse(node.right, low, high)

            elif node.val < low:
                traverse(node.right, low, high)
                
            elif node.val > high:
                traverse(node.left, low, high)
            
        traverse(root, low, high)

        return sum(stack)

        