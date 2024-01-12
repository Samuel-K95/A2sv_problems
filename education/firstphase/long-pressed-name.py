class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(Counter(name)) != len(Counter(typed)):
            return False
        first, second = 0, 0
        while first < len(name) and second < len(typed):
            if name[first] == typed[second]:
                first += 1
                second += 1
            else:
                while second < len(typed) and typed[second] == name[first - 1] and first > 0:
                    second += 1
                if second < len(typed):
                    if name[first] != typed[second]:
                        return False
        if first < len(name):
            return False
        while second < len(typed):
            if name[first-1] != typed[second]:
                return False
            second += 1
        return True  
