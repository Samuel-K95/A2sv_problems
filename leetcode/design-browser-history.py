class ListNode():
    def __init__(self, val=""):
        self.val = val
        self.next = None
        self.prev = None

class ListNode:

    def __init__(self, val = ""):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        dummy = ListNode()
        head = ListNode(homepage)

        dummy.next = head
        head.prev = dummy

        self.dummy = dummy
        self.head = head
        self.curr = head


    def visit(self, url: str) -> None:
        visit = ListNode(url)
        self.curr.next = visit
        visit.prev = self.curr
        self.curr = visit

    def back(self, steps: int) -> str:
        k = steps
        node = self.curr
        while k > 0 and node.prev != self.dummy:
            node = node.prev
            k -= 1
        self.curr = node
        return node.val

    def forward(self, steps: int) -> str:
        i = 0
        node = self.curr
        flag = False
        for i in range(steps):
            if not node.next:
                flag = True
                break
            node = node.next
        self.curr = node
        return node.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)