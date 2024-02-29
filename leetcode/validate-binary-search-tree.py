# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            traversal = []
            if not node:
                return []
            if not node.right and not node.left:
                return [node.val]
            if node.left:
                traversal.extend(inorder(node.left))
            traversal.append(node.val)
            if node.right:
                traversal.extend(inorder(node.right))
            return traversal
        answer = inorder(root)

        for i in range(1, len(answer)):
            if answer[i] <= answer[i-1]:
                return False
        return True