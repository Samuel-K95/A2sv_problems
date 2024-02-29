# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        isFound = None
        ans = None

        def traverse(node, p, q):
            nonlocal isFound
            nonlocal ans
            if not node:
                return False

            if node.val == p.val or node.val == q.val:
                if isFound == None:
                    isFound = node
                return True

            left = traverse(node.left, p, q)
            right = traverse(node.right, p, q)

            if left and right:
                ans = node
                return True
            elif left or right:
                return True
            else:
                return False

        if traverse(root, p, q) and ans:
            return ans
        else:
            return isFound

