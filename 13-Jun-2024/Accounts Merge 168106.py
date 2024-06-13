# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFindex_:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}
    
    def findex_(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x, y):
        repx = self.findex_(x)
        repy = self.findex_(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        group = UnionFindex_(len(accounts))
        mp_ = defaultdict(int)


        
        for i in range(len(accounts)):
            index_ = group.findex_(i)
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in mp_:
                    index_ = group.findex_(mp_[accounts[i][j]])
                    group.union(i, index_)

            for j in range(1, len(accounts[i])):
                mp_[accounts[i][j]] = i
                
        
        store = defaultdict(list)
        for i in group.parent:
            store[group.findex_(i)].append(i)

        ans = []
        for i in store:
            temp_ = []
            for j in store[i]:
                temp_.extend(accounts[j][1:])
            temp_ = set(temp_)
            temp_ = sorted(list(temp_))
            ans.append([accounts[i][0]] + temp_)

        return ans


        