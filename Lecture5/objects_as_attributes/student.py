class Student:
    def __init__(self, name: str, student_number: str, credits: int):
        self.name = name
        self.student_number = student_number
        self.credits = credits

    def add_credits(self, study_credits):
        if study_credits > 0:
            self.credits += study_credits

"""
print("Sally")
sally = Student("Sally Student", "12345", 0)
sally.add_credits(5)
sally.add_credits(5)
sally.add_credits(10)
print("Study credits:", sally.credits)


print("Mary")
mary = Student("Mary AlsoStudent", "23456", 0)
mary.credits = -100
print("Study credits:", mary.credits)"""