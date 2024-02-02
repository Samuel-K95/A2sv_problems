# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        target = ListNode(val = None, next = None)
        curr = target
        prev = curr
        if not list1 and not list2:
            return list1
        while list1 and list2:
            if list1.val <= list2.val:
                curr.val = list1.val
                list1=list1.next
            else:
                curr.val =list2.val
                list2=list2.next
            prev = curr
            temp = ListNode(val = None, next=None)
            curr.next = temp
            curr = curr.next
        while list1:
            temp = ListNode(val = None, next=None)
            curr.val = list1.val
            curr.next = temp
            prev = curr
            curr = curr.next
            list1=list1.next
        while list2:
            temp = ListNode(val = None, next=None)
            curr.val = list2.val
            curr.next=temp
            prev = curr
            curr = curr.next
            list2=list2.next
        prev.next=None
        return target
        
