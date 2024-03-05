# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        store = defaultdict(int)
        def dfs(node, r, val):
            nonlocal ans
            if not node:
                return
            if r in store:
                ans = max(ans, (val - store[r] + 1))
            else:
                store[r] = val
            return dfs(node.left, r+1, 2 * val) or dfs(node.right, r+1, (2*val) + 1)

        dfs(root, 0, 0)   

        return ans if ans != float('-inf') else 1

        