# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        if not left:
            return None
        right = left.next
        while left and right:
            if left.val == right.val:
                left.next = right.next
            else:
                left = left.next
            right = right.next
        return head
                


            
