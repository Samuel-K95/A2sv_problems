class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = float('-inf')
        for right in range(len(num) - 2):
            if right + 2 < len(num) and num[right] == num[right + 1] == num[right + 2]:
                curr = max(int(num[right]), curr)
        return (str(curr)*3) if curr != float('-inf') else ""
        