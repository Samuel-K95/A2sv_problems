# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}
        self.size = {i:1 for i in range(1, n+1)}
    
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edgetype = defaultdict(list)
        alice = UnionFind(n)
        bob = UnionFind(n)
        cnt = 0

        for t, u, v in edges:
            edgetype[t].append([u, v])

        for edge in edgetype[3]:
            u, v = edge
            repx = alice.find(u)
            repy = alice.find(v)

            if repx != repy:
                alice.union(u, v)
                bob.union(u, v)
                cnt +=1 

        for edge in edgetype[1]:
            u, v = edge
            repx = alice.find(u)
            repy = alice.find(v)

            if repx != repy:
                cnt += 1
                alice.union(u, v)

        for edge in edgetype[2]:
            u, v = edge
            repx = bob.find(u)
            repy = bob.find(v)

            if repx != repy:
                cnt += 1
                bob.union(u, v)


        al_set = set()

        for u in alice.parent:
            rep = alice.find(u)
            al_set.add(rep)
        
        bob_set = set()
        for u in bob.parent:
            rep = bob.find(u)  
            bob_set.add(rep)

        if len(al_set) > 1 or len(bob_set) > 1:
            return -1

        return len(edges) - cnt  

                







        

