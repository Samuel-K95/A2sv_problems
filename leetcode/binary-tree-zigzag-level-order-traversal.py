# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        if root:
            store[0].append(root.val)

        def recur(node, d):
            if not node:
                return 0
            
            if node.left:
                temp = recur(node.left, d + 1)

                store[d].append(temp.val)
            if node.right:
                temp = recur(node.right, d + 1)
                store[d].append(temp.val)

            return node
        recur(root, 1)
        
        store = sorted(store.items(), key = lambda x: x[0])

        ans = []
        for i in store:
            if i[0] % 2 != 0:
                i[1].reverse()

            ans.append(i[1])
        
        return ans
