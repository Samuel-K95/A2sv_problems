# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB
        check = set()
        while first and second:
            if first in check:
                return first
            if second in check:
                return second
            

            check.add(first)
            if second in check:
                return second
            check.add(second)

            first = first.next
            second = second.next

        while first:
            if first in check:
                return first

            first = first.next
        
        while second:
            if second in check:
                return second

            second = second.next

        return