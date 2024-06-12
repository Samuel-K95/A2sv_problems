# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(typed)
        first, second = 0,0
        while first < len(name) and second < n:
            if typed[second] == name[first]:
                first += 1
            elif typed[second] != name[first-1]:
                return False
            elif typed[second] != name[first] and first - 1 < 0:
                return False
            second += 1
        
        while second < n:
            if typed[second] != name[first-1]:
                return False
            second += 1
        
        if len(typed) < len(name):
            return False
        
        return True if first == len(name) else False
        