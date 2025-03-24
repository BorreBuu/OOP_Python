class TrainCarriage:

    def __init__(self, id: str, seats: int):
        self.id = id
        self.seats = seats
        self.reservation_situation = []

        if self.seats >= 0:
            self.create_carriage_seats(seats)
        else:
            print("could not create carriage, seat number not possible")

    def create_carriage_seats(self, seats):
        if seats > 0:
            for _ in range(seats):
                self.reservation_situation.append(0)
            #print(self.reservation_situation)

    def reserve_seat(self, seatno):
        if seatno > 0 and seatno <= self.seats:
            if self.reservation_situation[seatno-1] != 1:
                self.reservation_situation[seatno-1] = 1
                return None
            else:
                return "Seat already taken"
        else:
            return f"Seat number must be between 1 and {self.seats}"
        #print(self.reservation_situation)

    def remove_reservation(self, seatno):
        if seatno > 0 and seatno <= self.seats:
            if self.reservation_situation[seatno-1] != 0:
                self.reservation_situation[seatno-1] = 0
            else:
                print("Seat was already free, make sure you entered correct seat number")
        else:
            print(f"Seat number must be between 1 and {self.seats}")
        print(self.reservation_situation)

    def reset_reservations(self):
        for i in range(self.seats):
            self.reservation_situation[i] = 0
        print(self.reservation_situation)

    def report(self):
        list_of_seats = []
        carriage_situation = []
        for i in range(self.seats):
            list_of_seats.append(i+1)
            if self.reservation_situation[i] == 0:
                carriage_situation.append("[ ]")
            else:
                carriage_situation.append("[x]")
        print(f"report of the booking statuses in carriage {self.id}")
        print(*list_of_seats, sep='\t')
        print(* carriage_situation, sep='\t')

    def carriage_has_seats(self):
        if 0 in self.reservation_situation:
            print(f"Carriage {self.id} has seats available")
        else:
            print(f"Carriage {self.id} is full")

    def get_seat_availability(self):
        return self.carriage_has_seats()

    def get_carriage_info(self):
        return {"id": self.id,
                "seats": self.seats,
                "reservation_situation": self.reservation_situation
                }
    
    def __str__(self):
        return f"{self.id}: {self.reservation_situation}"


class Train:
    def __init__(self, train_id, locomotive):
        self.train_id = train_id
        self.carriages = []
        self.add_carriage(TrainCarriage(locomotive, 1))
        self.departure_location = None
        self.destination = None

    def add_carriage(self, carriage: TrainCarriage):
        if carriage not in self.carriages:
            self.carriages.append(carriage)
        else:
            print("Carriege is already added")
        #for carriage in self.carriages:
            #print(carriage)

    def remove_carriage(self, carriage_id):
        for i in range(len(self.carriages)):
            carriage = self.carriages[i]
            if carriage.id == carriage_id:
                self.carriages.pop(i)
                return f"carriage {carriage_id} removed"

        """
        Or this way:
        for i, carriage in enumerate(self.carriages):
            if carriage.id == carriage_id:
                self.carriages.pop(i)
                return f"carriage {carriage_id} removed"
        """
        return"Carriage is not part of this train"

    def reserve_seat(self, carriage_id, seat_no):
        for carriage in self.carriages:
            if carriage.id == carriage_id:
                result = carriage.reserve_seat(seat_no)
                if result:
                    return result
                else:
                    return f"reservation in carriage {carriage_id}, seat {seat_no} was successful"
        return "No such carriage in this train"

    def set_departure_location(self, location):
        self.departure_location = location
        print(f"Departure location set to {location}")

    def set_destination(self, destination):
        self.destination = destination
        print(f"Destination set to {destination}")

    def change_departure_location(self, location):
        self.departure_location = location
        print(f"Departure location changed to {location}")

    def change_destination(self, destination):
        self.destination = destination
        print(f"Destination changed to {destination}")

    def reset_departure_location(self):
        self.departure_location = None
        print("Departure location reset")

    def reset_destination(self):
        self.destination = None
        print("Destination reset")

    def train_report(self):
        for carriage in self.carriages:
            carriage.report()

    def get_train_info(self):
        return{
            "train_id": self.train_id,
            "departure_location": self.departure_location,
            "destination": self.destination,
            "carriages": [carriage.get_carriage_info() for carriage in self.carriages]
        }

    def __str__(self):
        carriage_info = [f"{carriage.id}: {carriage.reservation_situation}" for carriage in self.carriages]
        return (
            f"Train {self.train_id}\n"
            + f"Departure location: {self.departure_location}\n"
            + f"Destination: {self.destination}\n"
            + "With carriages:\n" + "\n".join(carriage_info)
            )

class TrainManager:
    def __init__(self):
        self.trains = []

    def add_train(self, train: Train):
        while any(existing_train.train_id == train.train_id for existing_train in self.trains):
            print(f"Train ID {train.train_id} already exists. Please choose a unique ID.")
            train.train_id = input("Enter a unique Train ID: ")

        self.trains.append(train)

    def print_all_trains(self):
        for train in self.trains:
            print(train)
            print()

    def __str__(self):
        return "\n".join(str(train) for train in self.trains)


if __name__ == "__main__":
    train_manager = TrainManager()
    #carriage1 = TrainCarriage("12A", 8)
    #carriage1.reserve_seat(2)
    #carriage1.reserve_seat(3)
    #carriage1.reserve_seat(8)
    #carriage1.remove_reservation(9)
    #carriage1.report()
    #carriage1.reset_reservations()
    #for i in range(8):
    #    carriage1.reserve_seat(i+1)
    #carriage1.report()
    #carriage1.carriage_has_seats()
    train1 = Train("MrBIG7", "L1")
    train_manager.add_train(train1)
    train1.add_carriage(TrainCarriage("56C", 4))
    train1.add_carriage(TrainCarriage("12A", 8))
    #train1.add_carriage(TrainCarriage("24A", 16))
    print(train_manager)
    #print(train1.remove_carriage("12A"))
    #print(train1)
    print(train1.reserve_seat("12A", 6))
    print(train1.reserve_seat("12A", 8))
    print(train1.reserve_seat("12A", 9))
    train1.train_report()
    train2 = Train("MadamLoco", "L4")
    train_manager.add_train(train2)
    #print(train_manager)

    train1.set_departure_location("Helsinki")
    train1.set_destination("Turku")
    #print(train1)

    #train1.change_departure_location("Tampere")
    #train1.change_destination("Oulu")
    #print(train1)

    #train1.reset_departure_location()
    #train1.reset_destination()
    #print(train1)
    print()
    train_manager.print_all_trains()
