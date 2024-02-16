# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        count = 0
        while node:
            node = node.next
            count += 1
        av = count // k
        rem = count % k
        ans = []
        node = head
        for i in range(k):
            if rem > 0:
                l = av + 1
            else:
                l = av
            smallhead = ListNode()
            tmp = smallhead
            while l and node:
                small = ListNode(node.val)
                tmp.next = small
                tmp = tmp.next
                node = node.next
                l -= 1
            ans.append(smallhead.next)
            rem -= 1
        return ans