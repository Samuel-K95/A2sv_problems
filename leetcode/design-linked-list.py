class Node:

    def __init__(self, val=-1):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        

    def get(self, index: int) -> int:
        temp = self.head
        for i in range(index + 1):
            if temp:
                temp = temp.next
            else:
                break

        if not temp:
            return -1
        else:
            return temp.val
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        temp=self.head
        newNode = Node(val)
        for i in range(index):
            if temp:
                temp=temp.next
            else:
                break
        if temp:
            newNode.next = temp.next
            temp.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                break
        if temp and temp.next:
            temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)