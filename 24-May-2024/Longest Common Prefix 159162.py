# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for ltr in word:
            idx = ord(ltr) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_end = True
    
    def search_pref(self, word):
        curr = self.root
        for i, ltr in enumerate(word):
            idx = ord(ltr) - ord('a')
            if curr.children[idx] == None:
                return i
            
            curr = curr.children[idx]
        return len(word)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insert(strs[0])
        ans = float('inf')

        for i in range(1, len(strs)):
            curr = trie.search_pref(strs[i]) 
            ans = min(curr, ans)

        return strs[0][:ans] if len(strs[0]) >= ans else strs[0]       