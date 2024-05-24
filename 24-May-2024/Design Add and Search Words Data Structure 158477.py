# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
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


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        def dfs(trie, curr, depth):
            if not trie:
                return False
            
            if depth == len(word)-1:
                if word[depth] == '.' or word[depth] == curr:
                    return trie.is_end
                else:
                    return False
                
            if word[depth] != '.' and (depth >= 0 and word[depth] != curr):
                return False
            
            
            curr = False
            for i in range(26):
                child = trie.children[i]
                if child != None:
                    curr = curr or dfs(child, chr(i + 97), depth+1)
            
            return curr
        trie = self.trie.root

        return dfs(trie, 0, -1)
        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)