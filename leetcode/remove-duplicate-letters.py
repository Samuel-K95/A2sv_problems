class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        vis = set()

        last_occ = defaultdict(int)

        for i in range(len(s)):
            last_occ[s[i]] = i

        for i in range(len(s)):
            while stack and stack[-1] > s[i]:
                if last_occ[stack[-1]] > i and s[i] not in vis:
                    vis.remove(stack[-1])
                    stack.pop()
                else:
                    break

            if s[i] not in vis:
                stack.append(s[i])
                vis.add(s[i]) 

        return "".join(stack)