class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        store = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                store[i+j].append(mat[i][j])
        
        ans = []
        for i in range(len(store)):
            tmp = store[i]
            if i % 2 == 0:
                tmp.reverse()
            ans.extend(tmp)
        return ans
