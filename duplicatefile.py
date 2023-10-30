class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        store = {}
        for i in paths:
            temp = i.split(" ")
            for j in range(1, len(temp)):
                dir = temp[0] + "/" + temp[j][: temp[j].index("(")]
                cont = temp[j][temp[j].index("(") : temp[j].index(")")]
                try:
                    store[cont].append(dir)
                except:
                    store[cont] = [dir]
        ans = []
        for key, value in store.items():
            if len(value) < 2:
                continue
            else:
                ans.append(value)

        return ans
