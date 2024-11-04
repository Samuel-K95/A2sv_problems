# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        fin = []
        ans = []
        for i in range(len(s)):
            if s[i] == ']':
                temp = []
                while ans and ans[-1] != '[':
                    temp.append(ans.pop())
                num = []
                ans.pop()
                while ans and ans[-1] in nums:
                    num.append(ans.pop())
                num.reverse()
                num =  int("".join(num)) if num else 1
                temp.reverse()
                ans.extend(temp * num)
            else:
                ans.append(s[i])

        return "".join(ans)
