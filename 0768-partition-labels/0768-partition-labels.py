class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        length = 0
        left = 0
        ans = []
        for i in range(len(s)):
            store[s[i]] = i
        for right in range(len(s)):
            length = max(store[s[right]], length)
            if right == length:
                ans.append(length - left + 1)
                left = length + 1
        return ans
