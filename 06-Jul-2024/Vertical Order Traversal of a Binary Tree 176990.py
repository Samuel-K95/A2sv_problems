# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        collect = defaultdict(list)

        def trav(node, col, row):
            if not node:
                return

            collect[col].append([row, node.val])
            
            trav(node.left, col - 1, row+1)
            trav(node.right, col + 1, row+1)

            return node
        trav(root, 0, 0)

        collect = sorted(collect.items(), key = lambda x: x[0])

        answer = [i[1] for i in collect]
        
        for i in range(len(answer)):

            answer[i].sort()

            for j in range(len(answer[i])):
                answer[i][j] = answer[i][j][1]

        return answer
