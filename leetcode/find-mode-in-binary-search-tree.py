# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def traverse(node):
            count[node.val] += 1
            if not node.left and not node.right:
                return
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        ans = sorted(count.items(), key = lambda x: x[1], reverse = True)

        maximum = ans[0][1]

        store = []
        for i in range(len(ans)):
            if ans[i][1] != maximum:
                break
            store.append(ans[i][0])
            
        return store

