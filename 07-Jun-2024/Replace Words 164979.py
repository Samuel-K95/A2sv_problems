# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')

            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_end = True
    
    def search(self, word):
        collect = []
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            
            if curr.is_end:
                return "".join(collect)

            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
            collect.append(c)

        return "".join(collect)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        words = sentence.split()
        ans = []

        for word in words:
            curr = trie.search(word)
            ans.append(curr)
        
        return " ".join(ans)

        