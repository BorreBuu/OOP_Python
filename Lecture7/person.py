class Person: #base class

   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email

   def update_email_domain(self, new_domain: str):
       old_domain = self.email.split("@")[1]
       self.email = self.email.replace(old_domain, new_domain)


class Student(Person): #in the parenthesis we have the base class name

   """ def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
       self.credits = credits """

   def __init__(self, name: str, id: str, email: str, credits: str):
       super().__init__(name, email)
       self.credits = credits
       self.id = id


class Teacher(Person):

   """ def __init__(self, name: str, email: str, room: str, teaching_years: int):
       self.name = name
       self.email = email
       self.room = room
       self.teaching_years = teaching_years """

   def __init__(self, name: str, email: str, room: str, teaching_years: int):
       super().__init__(name, email)
       self.room = room
       self.teaching_years = teaching_years

# Let's test our classes
if __name__ == "__main__":
   saul = Student("Saul Student", "1234", "saul@example.com", 0)
   saul.update_email_domain("example.edu")
   print(saul.email)

   tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
   tara.update_email_domain("example.ex")
   print(tara.email)