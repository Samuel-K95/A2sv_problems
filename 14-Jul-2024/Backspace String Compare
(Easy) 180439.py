# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks, stackt = [], []

        for i in s:
            if i == '#':
                if stacks:
                    stacks.pop()
            else:
                stacks.append(i)
        
        for i in t:
            if i == '#':
                if stackt:
                    stackt.pop()
            else:
                stackt.append(i)
        
        while stacks and stackt:
            fs, ft = stacks.pop(), stackt.pop()
            if fs != ft:
                return False
        
        return True if not stacks and not stackt else False