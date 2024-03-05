class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2":"abc",  "3":"def",
            "4":"ghi", "5": "jkl", "6":"mno",
            "7":"pqrs","8":"tuv",  "9":"wxyz"
        }
        temp = []
        ans = []

        def backtrack(i, j):
            s=""

            if j < len(digits):
                s = map[digits[j]]

            if j == len(digits)-1:
                for k in range(len(s)):
                    temp.append(s[k])
                    ans.append("".join(temp))
                    temp.pop()
                return

            curr = s
            for l in range(len(curr)):
                temp.append(curr[l])
                backtrack(l, j+1)
                temp.pop()

        backtrack(0, 0)
        
        return ans

