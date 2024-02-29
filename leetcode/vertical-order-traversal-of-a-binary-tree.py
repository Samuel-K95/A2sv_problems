# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)

        def recur(node, col, row):
            if not node:
                return

            store[col].append([row, node.val])
            recur(node.left, col - 1, row+1)
            recur(node.right, col + 1, row+1)

            return node
        recur(root, 0, 0)
        store = sorted(store.items(), key = lambda x: x[0])

        ans = [i[1] for i in store]
        
        for i in range(len(ans)):
            ans[i].sort()
            for j in range(len(ans[i])):
                ans[i][j] = ans[i][j][1]

        return ans
