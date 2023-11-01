class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boat = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            elif people[left] + people[right] <= limit:
                right -= 1
                left += 1
            boat += 1
        return boat

