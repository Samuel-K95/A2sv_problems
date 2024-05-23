# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for ltr in word:
            idx = ord(ltr) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ltr in word:
            idx = ord(ltr) - ord('a')

            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]

        return curr.is_end        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ltr in prefix:
            idx = ord(ltr) - ord('a')

            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True        

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)