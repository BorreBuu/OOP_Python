"""
class Property:
    def __init__(self, **kwargs):
        self.square_meter = kwargs.get('square_meter', 0.0)
        self.num_bedrooms = kwargs.get('beds', 0)
        self.num_baths = kwargs.get('baths', 0)
"""
class Property:
    valid_answers = ("yes", "no")

    def __init__(self, square_meter: float, beds: int, baths: int):
        self.square_meter = square_meter
        self.num_bedrooms = beds
        self.num_baths = baths
    
    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"square meters: {self.square_meter:.2f}")
        print(f"bedrooms: {self.num_bedrooms}")
        print(f"bathrooms: {self.num_baths}")

    """def prompt_init():
        return dict(square_meter=input("Enter the square meter: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)"""

    @classmethod
    def prompt_init(cls):
        square_meter = float(input("Enter the square meter: "))
        beds = int(input("Enter number of bedrooms: "))
        baths = int(input("Enter number of baths: "))
        return {"square_meter": square_meter, "beds": beds, "baths": baths}
    
    @staticmethod
    def get_valid_input(input_string, valid_options):
        input_string += f"({'/'.join(valid_options)}) "
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response
    

class Apartment(Property):
    """
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    """
    def __init__(self, square_meter: float, beds: int, baths: int, balcony = '', laundry = ''):
        super().__init__(square_meter, beds, baths)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("Laundry: ", self.laundry)
        print("Balcony: ", self.balcony)
   
    @classmethod
    def prompt_init(cls):
        parent_init = Property.prompt_init()
        laundry = cls.get_valid_input(
            "Does the apartment building have laundry?",
            Apartment.valid_answers)
        balcony = cls.get_valid_input(
            "Does the property have balcony? ",
            Apartment.valid_answers)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

class House(Property):
    valid_carage = ("attached", "detached", "none")

    def __init__(self, square_meter, beds, baths, num_stories = '', garage = '', fenced = ''):
        super().__init__(square_meter, beds, baths)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print(f"# of stories: {self.num_stories}")
        print(f"garage: {self.garage}")
        print(f"fenced yard: {self.fenced}")

    @classmethod
    def prompt_init(cls):
        parent_init = Property.prompt_init()
        fenced = cls.get_valid_input(
            "Is the yeard fenced? ",
            House.valid_answers)
        garage = cls.get_valid_input(
            "Is there a garage? ",
            House.valid_carage)
        num_stories = input("How many stories the house has? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    
class Purchase:
    def __init__(self, price = 0.0, taxes = 0.0):
        self.price = float(price)
        self.taxes = float(taxes)
    
    def display(self):
        print("PURCHASE DETAILS")
        print(f"Selling price: {self.price:.2f}")
        print(f"Estimated taxes: {self.taxes:.2f}")

    @classmethod
    def prompt_init(cls):
        price = float(input("What is the selling price? "))
        taxes = float(input("What are the estimated taxes? "))
        return {"price": price, "taxes": taxes}
    
class Rental:
    def __init__(self, furnished = '', utilities = 0.0, rent = 0.0):
        self.furnished = furnished
        self.rent = float(rent)
        self.utilities = float(utilities)

    def display(self):
        print("RENTAL DETAILS")
        print(f"Rent: {self.rent:.2f}")
        print(f"Estimated utilities: {self.utilities:.2f}")
        print(f"Furnished: {self.furnished}")

    @classmethod
    def prompt_init(cls):
        rent = float(input("What is the monthly rent? "))
        utilities = float(input("What are the estimated utilities? "))
        furnished = input("Is the property furnished? (yes/no)")
        return {"rent": rent, "utilities": utilities, "furnished": furnished}
    
if __name__ == "__main__":
    """property_details = Property.prompt_init()
    print(property_details)
    property = Property(**property_details)
    property.display()"""

    apartment_details = Apartment.prompt_init()
    print(apartment_details)
    apartment = Apartment(**apartment_details)
    apartment.display()

    """house_details = House.prompt_init()
    print(house_details)
    house = House(**house_details)
    house.display()

    purchase_details = Purchase.prompt_init()
    print(purchase_details)
    purchase = Purchase(**purchase_details)
    purchase.display()"""
    
    rental_details = Rental.prompt_init()
    print(rental_details)
    rental = Rental(**rental_details)
    rental.display()