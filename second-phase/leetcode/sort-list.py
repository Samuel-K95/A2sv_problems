# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []

        node = head
        while node:
            store.append(node.val)
            node = node.next
        
        
        def merge(arr):
            if len(arr) == 1:
                return arr
            
            if not arr:
                return []
            
            tot = len(arr)
            left = merge(arr[:tot//2])
            right = merge(arr[tot//2:])

            merged = []

            first, second = 0, 0

            while first < len(left) and second < len(right):
                if left[first] <= right[second]:
                    merged.append(left[first])
                    first += 1
                else:
                    merged.append(right[second])
                    second += 1
            

            merged.extend(left[first:])
            merged.extend(right[second:])

            return merged

        store = merge(store)
        if store:
            head = ListNode(store[0])
            node = head
            for i in range(1, len(store)):
                temp = ListNode(store[i])
                node.next = temp
                node=node.next
        return head


