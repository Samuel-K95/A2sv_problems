# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x
    
    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        group = UnionFind(n)
        for u, v in edges:
            group.union(u, v)
        

        rep_count = defaultdict(int)

        for i in range(n):
            rep = group.find(i)
            rep_count[rep] += 1
        
        if len(rep_count) == 1:
            return 0
            
        vals = sum(rep_count.values())
        vals = vals ** 2
        vals -= sum(curr ** 2 for curr in rep_count.values())

        return vals // 2
        