from phonebook import PhoneBook
from file_handler import FileHandler

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = filename

        for name,numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)


    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")


    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_number(name)
        if numbers == None:
            print("unknown number")
            return
        for number in numbers:
            print(number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()

application = PhoneBookApplication()
application.execute()