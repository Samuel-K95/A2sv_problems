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

        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_end = True
    
    def dfs(self, node, asc):
        if node.is_end == False:
            return []
        
        mx = []
        for idx in range(26):
            child = node.children[idx]
            if child and child.is_end:
                ret = self.dfs(child, idx)
                if len(ret) > len(mx):
                    mx = ret
        
        return [chr(asc + 97)] + mx

        



class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        longest = []
        for i in range(26):
            child = trie.root.children[i]
            if child:
                curr = trie.dfs(child, i)
                if len(curr) > len(longest):
                    longest = curr

        return "".join(longest)
