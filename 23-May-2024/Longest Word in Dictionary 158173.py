# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for chr in word:
            idx = ord(chr) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for chr in word:
            idx = ord(chr) - ord('a')
            if curr.children[idx] == None:
                return False
            
            curr = curr.children[idx]
        return curr.is_end

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = ""
        
        def dfs(node, word):
            nonlocal ans
            if not node:
                return

            for idx, child in  enumerate(node.children):
                if child and child.is_end:
                    if len(word + [chr(idx + 97)] ) > len(ans):
                        ans = "".join(word + [chr(idx + 97)])

                    dfs(child, word + [chr(idx + 97)])
                    
            return
        
        dfs(trie.root, [])

        return ans
            

            