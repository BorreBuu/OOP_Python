class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_number(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]
    
    def all_entries(self):
        return self.__persons


phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_number("Eric"))
