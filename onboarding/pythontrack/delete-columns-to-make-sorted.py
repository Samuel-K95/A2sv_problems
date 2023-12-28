class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        check = defaultdict(int)
        for i in range(len(strs)- 1):
            for j in range(len(strs[i])):
                if ord(strs[i][j]) > ord(strs[i+1][j]):
                    check[j] += 1
        return len(check)