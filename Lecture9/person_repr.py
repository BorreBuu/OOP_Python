class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    """
    Notice how the __repr__ method itself uses the repr function to retrieve the technical 
    representation of the string. This is necessary to include the ' characters in the result.
    """
    
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"
    
    """ def __str__(self):
        return f"{self.name} ({self.age} years)" """
    
person1 = Person("Anna", 25)
person2 = Person("Peter", 99)
print(person1)
print(person2)

""" Person = Person("Ellie", 34)
print(Person)
print(repr(Person)) """

#string representation of the list is always __repr__
""" persons = []
persons.append(Person("Anna", 25))
persons.append(Person("Peter", 99))
persons.append(Person("Mary", 55))
print(persons) """