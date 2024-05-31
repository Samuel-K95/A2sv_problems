# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number):
        curr = self.root

        for i in range(31, -1, -1):
            curr_bit = number & (1 << i)
            if curr_bit > 0:
                if curr.children[1] == None:
                    curr.children[1] = TrieNode()
                curr = curr.children[1]
            else:
                if curr.children[0] == None:
                    curr.children[0] = TrieNode()
                curr = curr.children[0]
        curr.is_end = True
    
    def search(self, number):
        curr = self.root
        track = 0
        for i in range(31, -1, -1):
            track *= 2
            if number & (1 << i) > 0:
                if curr.children[0] != None:
                    track += 0
                    curr = curr.children[0]
                else:
                    track += 1
                    curr = curr.children[1]
            else:
                if curr.children[1] != None:
                    track += 1
                    curr = curr.children[1]
                else:
                    track += 0
                    curr = curr.children[0]

        return number ^ track
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        trie = Trie()

        trie.insert(nums[0])
        for number in nums[1:]:
            ans = max(ans, trie.search(number))
            trie.insert(number)
        
        return ans

        


        

        