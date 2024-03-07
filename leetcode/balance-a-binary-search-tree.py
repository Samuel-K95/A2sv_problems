# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        store = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            store.append(node.val)
            inorder(node.right)

        inorder(root)

        def build(arr):
            if len(arr) == 0:
                return
            if len(arr) == 1:
                return TreeNode(arr[0])

            mid = len(arr) // 2

            node = TreeNode(arr[mid])

            node.left= build(arr[:mid])
            node.right = build(arr[mid+1:]) if mid + 1 < len(arr) else None


            return node

        return build(store)
