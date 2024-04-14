# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, state):
            nonlocal ans
            if node and not node.left and not node.right:
                if state == 0:
                    ans += node.val
                return

            if node.left:
                left = dfs(node.left, 0)
            
            if node.right:
                right = dfs(node.right, 1)
        
        dfs(root, -1)

        return ans
