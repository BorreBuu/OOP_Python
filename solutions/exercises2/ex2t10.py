class Property:
    def __init__(self, rooms: int , square_meters: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
 
    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters
 
    def price_difference(self, compared_to):
        # Funktio abs palauttaa itseisarvon
        ero = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return ero
 
    def more_expensive(self, compared_to):
        ero = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return ero > 0
    

if __name__ == "__main__":
    central_studio = Property(1, 16, 5500)
    downtown_two_bedroom = Property(2, 38, 4200)
    suburbs_three_bedroom = Property(3, 78, 2500)

     #Part 1
    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))
    print()

    #part2
    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))
    print()

    #part3
    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))
