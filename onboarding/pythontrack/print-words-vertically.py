class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = defaultdict(list)
        words = s.split()
        dup = [i for i in words]
        dup.sort(key = lambda x: len(x))
        maxi = len(dup[-1])
        for i in range(maxi):
            for j in range(len(words)):
                try:
                    ans[i].append(words[j][i])
                except:
                    # if j >= len(words[j]):
                    ans[i].append(" ")
        fin = [""] * maxi
        for key, values in ans.items():
            fin[key] = "".join(ans[key]).rstrip()
        return fin

