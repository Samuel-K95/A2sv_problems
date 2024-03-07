# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(arr):
            if len(arr) == 0:
                return
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            max_ = arr[0]
            max_ind = 0
            
            for i in range(len(arr)):
                if arr[i] > max_:
                    max_ = arr[i]
                    max_ind = i
            node = TreeNode(max_)

            node.left = build(arr[:max_ind])
            node.right = build(arr[max_ind+1:]) if max_ind + 1 < len(arr) else None


            return node

        return build(nums)
