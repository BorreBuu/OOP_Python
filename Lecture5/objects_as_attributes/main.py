from completedcourse import CompletedCourse
from course import Course
from student import Student

students = []
students.append(Student("Ollie", "1234", 10))
students.append(Student("Peter", "2345", 23))
students.append(Student("Lena", "3456", 43))
students.append(Student("Tina", "4567", 8))

itp = Course("Introduction to Programming", "itp1", 5)
#aap = Course("Advanced application programming", "aap", 5)

completed = []
for student in students:
    completed.append(CompletedCourse(student, itp, 3))


for course in completed:
    print(course.student.name)
    print(course.course.name)
