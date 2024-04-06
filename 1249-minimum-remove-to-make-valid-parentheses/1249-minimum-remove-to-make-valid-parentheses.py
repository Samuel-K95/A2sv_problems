class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rem = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    rem.add(i)
        while stack:
            curr = stack.pop()
            rem.add(curr)
        
        ans = []
        for i in range(len(s)):
            if i not in rem:
                ans.append(s[i])
        return "".join(ans)

