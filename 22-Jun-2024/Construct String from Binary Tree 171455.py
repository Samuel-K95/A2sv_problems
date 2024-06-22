# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        

        def traverse(node):
            if not node:
                return
            
            left = traverse(node.left)
            right = traverse(node.right)

            if not left and not right:
                return f'{node.val}'
            
            if left and right:
                return f'{node.val}({left})({right})'
            
            if not left and right:
                return f'{node.val}()({right})'
            
            if left and not right:
                return f'{node.val}({left})'

        return traverse(root)



            