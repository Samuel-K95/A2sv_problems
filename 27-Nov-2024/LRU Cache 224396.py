# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.mp = defaultdict(Node)
        self.capacity = capacity
        self.left , self.right = Node(0, 0), Node(0, 0) 
        self.left.next = self.right
        self.right.prev = self.left
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.next, node.prev = None, None
    
    def insert(self, node):
        mru , nxt = self.right.prev, self.right
        mru.next, nxt.prev = node, node
        node.prev = mru
        node.next = self.right
        
    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])

        
        node = Node(key=key, val=value)
        self.mp[key] = node
        self.insert(node)

        if len(self.mp) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)