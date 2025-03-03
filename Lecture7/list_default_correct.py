class Student:
    def __init__(self, name, completed_courses=None):
        self.name = name
        if completed_courses is None:
            self.completed_courses = []
        else:
            self.completed_courses = completed_courses

    def add_course(self, course):
        self.completed_courses.append(course)


student1 = Student("Sally Student")
student2 = Student("Sassy Student")
student3 = Student("Perry Student", ["ACiP"])

student1.add_course("ItP")
student1.add_course("ACiP")

student3.add_course("ItP")

print(student1.completed_courses)
print(student2.completed_courses)
print(student3.completed_courses)