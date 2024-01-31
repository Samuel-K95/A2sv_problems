# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        right = head
        store = []
        while right:
            store.append(right.val)
            right = right.next
        store.reverse()
        node = head
        i = 0
        while node:
            node.val = store[i]
            node = node.next
            i += 1
        return head