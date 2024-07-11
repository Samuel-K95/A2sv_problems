# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ')':
                temp = []
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    temp.append(top)
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)
                
        return "".join(stack)