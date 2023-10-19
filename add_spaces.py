class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        space_count = 0
        for i in range(len(s)):
            if space_count < len(spaces) and spaces[space_count] == i:
                ans.append(" ")
                space_count += 1
                ans.append(s[i])
            else:
                ans.append(s[i])
        return "".join(ans)
