from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_d = deque(students)
        i = 0
        while students_d:
            if students_d[0] == sandwiches[i]:
                students_d.popleft()
                i += 1

            else:
                if sandwiches[i] in students_d:
                    students_d.append(students_d.popleft())
                else:
                    break

        return len(students_d)


print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(Solution().countStudents(
    students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
