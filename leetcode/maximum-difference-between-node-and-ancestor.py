# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def recur(node):
            nonlocal ans
            if not node:
                return [float('inf'), float('-inf')]

            if not node.left and not node.right:
                return [node.val, node.val]

            
            left = recur(node.left)
            right = recur(node.right)

            small = min(left[0], right[0])
            large = max(left[1], right[1])

            ans = max(abs(node.val - small), abs(node.val-large), ans)

            return [min(small, node.val), max(node.val, large)]
        
        recur(root)

        return ans
