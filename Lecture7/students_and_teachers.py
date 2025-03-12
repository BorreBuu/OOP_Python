class Student:

    def __init__(self, name: str, id: str, email: str, credits: str):
        self.name = name
        self.id = id
        self.email = email
        self.credits = credits

class Teacher:

    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name
        self.email = email
        self.room = room
        self.teaching_years = teaching_years

def update_student_email(o: Student):
    o.email = o.email.replace(".com", ".edu")

def update_teacher_email(o: Teacher):
    o.email = o.email.replace(".com", ".edu")