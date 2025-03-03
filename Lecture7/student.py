class Student:
    """ This class models a student """

    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = ""):
        # calling the setter method for the name attribute
        self.name = name

        # No setter method for the attribute student_number as the student number is not supposed to change!
        if len(student_number) < 5:
            raise ValueError("A student number should have at least five characters")

        self.__student_number = student_number

        # calling the setter method for the credits attribute
        self.credits = credits

        self.__notes = notes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def student_number(self):
        return self.__student_number

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, op):
        if op >= 0:
            self.__credits = op
        else:
            raise ValueError("The number of study credits cannot be below zero")

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    def summary(self):
        print(f"Student {self.__name} ({self.student_number}):")
        print(f"- credits: {self.__credits}")
        print(f"- notes: {self.notes}")

if __name__ == "__main__":
    # Passing only the name and the student number as arguments to the constructor
    student1 = Student("Sally Student", "12345")
    student1.summary()

    # Passing the name, the student number and the number of study credits
    student2 = Student("Sassy Student", "54321", 25)
    student2.summary()

    # Passing values for all the parameters
    student3 = Student("Saul Student", "99999", 140, "extra time in exam")
    student3.summary()

    # Passing a value for notes, but not for study credits
    # NB: the parameter must be named now that the arguments are not in order
    student4 = Student("Sandy Student", "98765", notes="absent in academic year 20-21")
    student4.summary()

    #student4.notes = "This is a new note"
    #student4.summary()