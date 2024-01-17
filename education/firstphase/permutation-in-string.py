class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        store = Counter(s1)
        check = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            check[s2[right]] += 1
            if (right - left + 1) == length:
                if check == store:
                    return True
                while left < len(s2) and right - left + 1 >= length:
                    check[s2[left]] -= 1
                    if check[s2[left]]  == 0:
                        del check[s2[left]] 
                    left += 1
        return False
