class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        front = 0
        back = len(skill) - 1
        skill.sort()
        target = skill[front] + skill[back]
        ans = 0
        while front <= back:
            if skill[front] + skill[back] != target:
                return -1
            else:
                ans += skill[front]  * skill[back]
                front += 1
                back -= 1
        return ans

