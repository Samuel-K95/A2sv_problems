class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        chem = skill[left] + skill[right]
        tot = 0
        while left <= right:
            if skill[left] + skill[right]  != chem:
                return -1
            else:
                tot += skill[left] * skill[right]
                left += 1
                right -= 1
        return tot