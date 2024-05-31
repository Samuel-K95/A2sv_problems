# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()   


    def max_xor(self, n, mx):
        curr = self.root
        track = 0

        for i in range(mx-1, -1, -1):
            track *= 2
            curr_bit = (1 << i) & n
            if curr_bit > 0:
                if curr.children[0] == None:
                    curr.children[0] = TrieNode()
                curr = curr.children[0]
                track += 0
            else:
                if curr.children[1] == None:
                    curr.children[1] = TrieNode()
                curr = curr.children[1]
                track += 1

        return track



class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        trie = Trie()
        n = len(nums)

        curr_xor = 0
        ans = []
        for i in nums:
            curr_xor ^= i
            
        while nums:
            search = trie.max_xor(curr_xor, maximumBit)
            ans.append(search)
            top = nums.pop()
            curr_xor ^= top

        return ans

        
