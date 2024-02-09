# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Dummy  = ListNode()
        dumhead = Dummy
        node = head
        count = 0
        
        while node:
            count += 1
            node = node.next
        targ = count - n
        node = head
        
        while targ:
            Dummy.next = node
            Dummy = Dummy.next
            node = node.next
            targ -= 1
        Dummy.next = node.next
        Dummy = node.next
        
        return dumhead.next
        