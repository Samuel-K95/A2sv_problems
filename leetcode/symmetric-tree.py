# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_stack = []
        right_stack = []
        if root.left and root.right and root.left.val != root.right.val:
            return False

        def inorder(node, lr):
            if not node:
                return None

            left = inorder(node.left, lr)
            if lr == 'l':
                if node.right and not node.left:
                    left_stack.append('null')
                left_stack.append(node.val)

            else:  
                if node.right and not node.left:
                    right_stack.append('null') 
                right_stack.append(node.val)

            right = inorder(node.right, lr)

            if node.left and not node.right and lr == 'l':
                left_stack.append('null')
            if node.left and not node.right and lr == 'r':
                right_stack.append('null')


        inorder(root.left, 'l')
        inorder(root.right, 'r')

        right_stack.reverse()

        return left_stack == right_stack

            