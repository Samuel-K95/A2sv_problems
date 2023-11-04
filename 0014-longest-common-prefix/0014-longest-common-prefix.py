class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def comp(a, b):
            if len(a) > len(b):
                return 1
            else:
                return -1

        store = sorted(strs, key=cmp_to_key(comp))
        ans = ""
        if len(strs) == 1:
            return strs[0]
        wor = ""
        for r in range(len(store[0])):
            wor += store[0][r]
            for j in range(1, len(store)):
                if store[j][: r + 1] != wor:
                    return ans
            ans = wor
        return ans