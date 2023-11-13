class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        for i in range(len(s)):
            store[s[i]] = i
        ans = []
        end = 0
        size = 0
        for right in range(len(s)):
            end = max(end,store[s[right]])
            size += 1
            if right ==  end:
                ans.append(size)
                size = 0
        return ans
