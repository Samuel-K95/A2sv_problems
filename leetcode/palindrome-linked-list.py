# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        comp = []
        node = head
        while node:
            comp.append(node.val)
            node = node.next
        comp.reverse()
        i = 0
        while head:
            if head.val != comp[i]:
                return False
            i += 1
            head= head.next
        return True
        