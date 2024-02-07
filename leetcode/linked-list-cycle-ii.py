# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        fast = head
        slow = head

        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag =True
                break

        if flag:
            slow = head
            while slow.next:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return