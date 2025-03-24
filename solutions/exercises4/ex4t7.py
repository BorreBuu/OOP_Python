class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
 
    def __str__(self):
        return self.name
 
class Room:
    def __init__(self):
        self.persons = []
 
    def add(self, person: Person):
        self.persons.append(person)
 
    def is_empty(self):
        return len(self.persons) == 0
 
    def print_contents(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')
 
    def shortest(self):
        shortest_person = None
        shortest_height = 0
        for person in self.persons:
            if shortest_person is None or person.height < shortest_height:
                shortest_person= person
                shortest_height = person.height
 
 
        return shortest_person
 
    def remove_shortest(self):
        # use the method above
        shortest_person = self.shortest()
        # this is the same as shortest_person is not None
        if shortest_person:
            self.persons.remove(shortest_person)
 
        return shortest_person
    
if __name__ == "__main__":
    #part 1
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 175))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
    print()

    #part 2
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    print()
    room.print_contents()
    print()

    #part 3
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
    print()
    room.print_contents()


