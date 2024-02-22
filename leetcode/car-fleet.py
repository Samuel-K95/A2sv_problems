class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x: x[0])

        hours = []

        for i in range(len(zipped)):
            hour = (target - zipped[i][0]) / zipped[i][1]
            hours.append(hour)

        for i in range(len(hours)):
            while stack and stack[-1] <= hours[i]:
                stack.pop()
            stack.append(hours[i])

        return len(stack)

