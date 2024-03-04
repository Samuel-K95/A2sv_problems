# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(nums):
            if len(nums) == 1:
                return TreeNode(nums[0])
            elif len(nums)  == 0:
                return
            
            curr = len(nums) // 2
            
            node = TreeNode(nums[curr])
            left = build(nums[:curr])
            right = build(nums[curr + 1:])

            node.left = left
            node.right = right

            return node
        
        return build(nums)

