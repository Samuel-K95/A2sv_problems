# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        isFound = None
        def traverse(node, p, q):
            if not node:
                return

            if node.val > p.val and node.val > q.val:
                return traverse(node.left, p, q)
            elif node.val < p.val and node.val < q.val:
                return traverse(node.right , p, q)
            else:
                return node

        return traverse(root, p, q)

                    
        