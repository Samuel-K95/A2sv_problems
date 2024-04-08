class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwitches = deque(sandwiches)
        ans = 0
        while students and sandwitches:
            front = sandwitches[0]
            temp = []
            while students and students[0] != front:
                curr = students.popleft()
                temp.append(curr)
            if not students:
                ans = len(temp)
                break
            elif students:
                sandwitches.popleft()
                students.popleft()
                students.extend(temp)
                
        return ans



