# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        dummy = ListNode(-1)
        node = dummy
        while node:
            fir, sec = 0, 0
            if not l1 and not l2 and rem == 0:
                break
            if l1:
                fir = l1.val
                l1 = l1.next
            if l2:
                sec = l2.val
                l2 = l2.next
            
            
            curr = fir + sec + rem
            rem, ans = 0, curr
            if len(str(curr)) > 1:
                ans = int(str(curr)[1])
                rem = int(str(curr)[0])
            new = ListNode(ans)
            node.next = new
            node = node.next

        return dummy.next



        