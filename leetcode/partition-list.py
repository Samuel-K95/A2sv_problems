# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        node = head
        before = ListNode(val=float('-inf'))
        while node and node.val < x:
            if before.val == float('-inf'):
                before.next = node
                before = before.next
                head = before
            else:
                before.next = node
                before = before.next
            node = node.next
        after = ListNode(val = float('inf'))
        dummy = after
        if node:
            after = node
            dummy = after
            node = node.next
        while node:
            if node.val < x:
                if before.val == float('-inf'):
                    before.next = node
                    before = before.next
                    head = before
                else:
                    before.next = node
                    before = before.next
            else:
                after.next = node
                after = after.next
            node = node.next
        if after.val != float('-inf'):
            after.next = None
            if dummy.val != float('inf'):
                before.next = dummy
        return head
