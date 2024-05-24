# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, state):
        curr = self.root

        for ltr in word:
            idx = ord(ltr) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr= curr.children[idx]
        curr.is_end = state
    
    def search(self, word):
        curr = self.root
        for i, ltr in enumerate(word):
            idx = ord(ltr) - ord('a')
            if curr.children[idx] == None:
                return -1
            curr = curr.children[idx]
            if curr.is_end:
                return i

        return len(word)-1
    


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []

        trie = Trie()
        for word in dictionary:
            trie.insert(word, True)
        
        sentence = sentence.split()
        for sub in sentence:
            ret = trie.search(sub)
            if ret == -1:
                ans.append(sub)
                trie.insert(sub, False)
            else:
                ans.append(sub[:ret + 1])

        
        return " ".join(ans)
