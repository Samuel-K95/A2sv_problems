# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = []
        def recur(node, d):
            if not node:
                return
                

            stack.append(str(node.val))

            if not node.left and not node.right:
                ans.append("".join(stack))

            left = recur(node.left, d+1)

            while len(stack) > d:
                stack.pop()

            right = recur(node.right, d+1)
            while len(stack) > d:
                stack.pop()
                   
        
        recur(root, 1)

        fin = 0
        for i in ans:
            fin += int(i)

        return fin