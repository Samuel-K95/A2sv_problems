class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        left = {'(', '[', '{'}
        for i in range(len(s)):
            if s[i] in left:
                check.append(s[i])
            else:
                if check:
                    last = check.pop()
                else:
                    return False
                if s[i] == ')' and last != '(':
                    return False
                elif s[i] =='}' and last != '{':
                    return False
                elif s[i] == ']' and last != '[':
                    return False
        if len(check) > 0:
            return False
        else:
            return True