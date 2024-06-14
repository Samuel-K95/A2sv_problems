# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class LinkNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.dummy = LinkNode()
        

    def get(self, index: int) -> int:
        idx = -1
        node = self.dummy

        while node and idx < index:
            node = node.next
            idx += 1
        
        if not node:
            return -1
        
        return node.val


    def addAtHead(self, val: int) -> None:
        nxt = self.dummy.next
        tmp = LinkNode(val)

        self.dummy.next = tmp
        tmp.prev = self.dummy
        tmp.next = nxt
        if nxt:
            nxt.prev = tmp
        

    def addAtTail(self, val: int) -> None:
        tmp = LinkNode(val)
        node = self.dummy
        while node and node.next:
            node = node.next
        node.next = tmp
        tmp.prev = node
        

        

    def addAtIndex(self, index: int, val: int) -> None:
        tmp = LinkNode(val)
        idx = -1
        node = self.dummy
        while idx < index - 1 and node:
            node = node.next
            idx += 1
        
        if not node:
            return
        
        nxt = node.next
        node.next = tmp
        tmp.prev = node
        tmp.next = nxt
        if nxt:
            nxt.prev = tmp


        

    def deleteAtIndex(self, index: int) -> None:
        idx = -1
        node = self.dummy
        while idx < index and node:
            node = node.next
            idx += 1
        
        if not node:
            return
        
        nxt = node.next
        prev = node.prev

        node.next , node.prev =  None, None

        prev.next = nxt
        if nxt:
            nxt.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)